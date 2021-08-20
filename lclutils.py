import sys
from icecream import ic
import sqlalchemy as dbsql
from sqlalchemy.orm import sessionmaker
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlQueryModel


class sqlpg:
    """
    connect to posgres on flatboy database rfile
    """

    def __init__(self) -> None:
        super(sqlpg, self).__init__()

    def pg_sql_connect(self):
        """
        create connection
        """
        self.eng = dbsql.create_engine("postgresql://rfile:simple@flatboy/rfile")
        self.conn = self.eng.connect()  # use this as connection for insert query
        if self.conn:
            return self.conn

    def pg_sql_session(self):
        self.pg_eng = dbsql.create_engine("postgresql://rfile:simple@flatboy/rfile")
        self.pg_mysession = sessionmaker(bind=self.eng)
        self.pg_mysess = self.pg_mysession()
        return self.pg_mysess

    def sqlite_sql_session(self):
        self.eng = dbsql.create_engine("sqlite:////data/sqlite/vitals.db")
        self.mysession = sessionmaker(bind=self.eng)
        self.mysess = self.mysession()
        return self.mysess

    def pgsql_insert_rec_vitals(self, connection, pg_table_name, txt_dict):
        """
        needs a table name connect name and
        list(dict) of items in correct order
        """
        self.conn = connection
        self.pg_table_name = pg_table_name
        self.txt_dict = txt_dict
        self.pg_table_name = dbsql.table(
            self.pg_table_name,
            dbsql.column("bpdate"),
            dbsql.column("bpsys"),
            dbsql.column("bpdia"),
            dbsql.column("bphr"),
            dbsql.column("bpsugar"),
            dbsql.column("bpoxy"),
            dbsql.column("bpcomment"),
        )
        self.ins = self.pg_table_name.insert().values(self.txt_dict)
        self.result = self.conn.execute(self.ins)
        if self.result:
            self.result_txt = "Rec Inserted PG:\n %s" % (self.pg_table_name)
            return self.result_txt

    def pg_sql_notes_update(self, connect, txt_dict, notes_table_name, maxid):
        self.notes_table_name = notes_table_name
        self.notes_conn = connect
        self.notes_txt_dict = txt_dict
        self.maxid = maxid
        self.notes_table = dbsql.table(
            self.notes_table_name,
            dbsql.column("foodid"),
            dbsql.column("fdate"),
            dbsql.column("sugarid"),
            dbsql.column("bpid"),
            dbsql.column("fnotes"),
        )
        self.notes_update = (
            self.notes_table.update()
            .where(self.notes_table.c.foodid == self.maxid)
            .values(self.notes_txt_dict)
        )

        self.notes_result = self.notes_conn.execute(self.notes_update)

    def pg_sql_notes_insert(self, connect, txt_dict, notes_table_name):
        """
        takes session name and dict to pass to table

        """
        self.notes_conn = connect
        self.notes_txt_dict = txt_dict
        self.notes_table_name = notes_table_name
        self.notes_table = dbsql.table(
            self.notes_table_name,
            dbsql.column("fdate"),
            dbsql.column("sugarid"),
            dbsql.column("bpid"),
            dbsql.column("fnotes"),
        )
        self.notes_ins = self.notes_table.insert().values(self.notes_txt_dict)
        self.notes_result = self.conn.execute(self.notes_ins)
