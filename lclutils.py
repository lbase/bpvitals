import sys
from icecream import ic
import sqlalchemy as dbsql
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlQueryModel


class sqlpg:
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
