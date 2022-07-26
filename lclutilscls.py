import sys
from icecream import ic

# import sqlalchemy as dbsql
from sqlalchemy.orm import sessionmaker

# from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlQueryModel
from PyQt5.QtCore import QSettings
from sqlalchemy.pool import StaticPool
from dataclasses import dataclass
from dataclasses import field
from typing import List

from sqlalchemy import column
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import table
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

mapper_reg = registry()


class Sqlpg:
    """
    connect to databases on flatboy postresql and
    sqlite database rfile
    """

    def __init__(self) -> None:
        super(Sqlpg, self).__init__()
        ic.disable()

    def pg_sql_connect(self):
        """
        create connection posgresql
        """
        self.eng = create_engine("postgresql://rfile:simple@flatboy/rfile")
        self.conn = self.eng.connect()  # use this as connection for insert query
        if self.conn:
            return self.conn

    def sl_sql_connect(self):
        """
        create connection sqlite
        """
        self.sl_eng = create_engine(
            "sqlite:///file:///data/sqlite/vitals.db?check_same_thread=true&timeout=10&mode=rw&nolock=1&uri=true"
        )
        self.sl_conn = self.sl_eng.connect()  # use this as connection for insert query
        if self.sl_conn:
            ic(self.sl_conn)
            return self.sl_conn

    def pg_sql_session(self):
        self.pg_eng = create_engine("postgresql://rfile:simple@flatboy/rfile")
        self.pg_mysession = sessionmaker(bind=self.eng)
        self.pg_mysess = self.pg_mysession()
        return self.pg_mysess

    def sqlal_table_mynotes(self, notes_table_name):
        self.notes_table_name = notes_table_name

        self.mynotes = table(
            self.notes_table_name,
            column("foodid"),
            column("fdate"),
            column("sugarid"),
            column("bpid"),
            column("fnotes"),
        )
        return self.mynotes

    def sqlal_table_vsigns(self, notes_table_name):
        """basic sqlalchemy table to use for update insert in
           vsigns_bp table in both databases
        """
        self.notes_table_name = notes_table_name
        self.vsigns = table(
            self.notes_table_name,
            column("bpid"),
            column("bpdate"),
            column("bpsys"),
            column("bpdia"),
            column("bphr"),
            column("bpsugar"),
            column("bpoxy"),
            column("bpcomment"),
        )
        return self.vsigns

    def sqlal_Table_qtsugar(self, notes_table_name):
        """basic sqlalchemy table structure for sugar tables
           both postgresql and sqlite
        """
        self.notes_table_name = notes_table_name
        self.mysugar = table(
            self.notes_table_name,
            column("bsid"),
            column("bsdate"),
            column("bsugar"),
            column("comment"),
        )
        return self.mysugar

    def pgsql_insert_rec_vitals(self, connection, pg_table_name, txt_dict):
        """
        needs a table name connect name and
        list(dict) of items in correct order
        """
        self.conn = connection
        self.pg_table_name = pg_table_name
        self.txt_dict = txt_dict
        self.pg_table_name = self.sqlal_table_vsigns(self.pg_table_name)
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
        self.notes_table = self.sqlal_table_mynotes(self.notes_table_name)
        self.notes_update = (
            self.notes_table.update()
            .where(self.notes_table.c.foodid == self.maxid)
            .values(self.notes_txt_dict)
        )

        self.notes_result = self.notes_conn.execute(self.notes_update)
        return self.notes_result

    def pg_sql_notes_insert(self, connect, txt_dict, notes_table_name):
        """
        takes session name and dict to pass to table name

        """
        self.notes_conn = connect
        self.notes_txt_dict = txt_dict
        self.notes_table_name = notes_table_name
        self.notes_table = self.sqlal_table_mynotes(self.notes_table_name)
        self.notes_ins = self.notes_table.insert().values(self.notes_txt_dict)
        self.notes_result = self.conn.execute(self.notes_ins)
        return self.notes_result

    def pg_sql_qtsugar_insert(self, connect, txt_dict, sugar_tablename):
        """takes connect dict of values to insert and tablename"""
        self.table_sugar = sugar_tablename
        self.sugar_conn = connect
        self.sugar_dict = txt_dict
        self.tbsugar = self.sqlal_table_qtsugar(self.table_sugar)
        self.sugar_ins = self.tbsugar.insert().values(self.sugar_dict)
        self.sugar_result = self.sugar_conn.execute(self.sugar_ins)


class Lite_Sql:
    def __init__(self) -> None:
        super(Lite_Sql, self).__init__()

    def sqlite_sql_session(self):
        self.eng = create_engine("sqlite:////data/sqlite/vitals.db")
        self.mysession = sessionmaker(bind=self.eng)
        self.mysess = self.mysession()
        return self.mysess


class BP_Settings:
    def __init__(self) -> None:
        super(BP_Settings, self).__init__()


@dataclass
class foodnotes:
    fdate: str
    fnotes: str
    sugarid: int
    bpid: int
