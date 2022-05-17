#! /usr/bin/env python3


from notes import Ui_Comment
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QDataWidgetMapper, QTableView
import sqlalchemy as dbsql
from sqlalchemy.orm import sessionmaker
from icecream import ic
from lclutils import Sqlpg
import sys


class Main(QtWidgets.QWidget, Ui_Comment):
    """docstring for Main
"""

    ic.disable()

    def __init__(
        self, object, table_name="foodnotes"
    ):  # foodnotes default table alternate is fastnotes
        super(Main, self).__init__()
        self.table_name = table_name
        self.ui = Ui_Comment()
        self.ui.setupUi(self)

        # self.conn_notes = self.eng.connect()  # use this as connection for insert query
        # ---------------------------------------------------------------------------- #
        #           make sqlalchemy session and database connection                    #
        # ---------------------------------------------------------------------------- #
        self.pg = Sqlpg()
        self.pg_conn = self.pg.pg_sql_connect()
        # self.conn = self.pg
        self.sqlite_conn = self.pg.sl_sql_connect()
        self.pg_sess = self.pg.pg_sql_session()
        self.eng = dbsql.create_engine("sqlite:////data/sqlite/vitals.db")
        self.mysession = sessionmaker(bind=self.eng)
        self.mysess = self.mysession()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("/data/sqlite/vitals.db")
        self.ok = self.db.open()
        ic(self.ok, self.db.driverName())

        # ---------------------------------------------------------------------------- #
        #              table name in window title so I can tell what table              #
        # ---------------------------------------------------------------------------- #
        self.setWindowTitle(self.table_name)
        # current date
        now = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(now)
        # buttons
        self.ui.btnAdd.clicked.connect(self.add_rec)
        self.ui.btnUpdate.clicked.connect(self.update_rec)
        self.ui.btnExit.clicked.connect(self.exitfunc)
        self.ui.chkPG.setCheckState(1)
        self.populate_boxes()
        # ---------------------------------------------------------------------------- #
        #                      get numbers and one previous record                     #
        # ---------------------------------------------------------------------------- #

    def populate_boxes(self):
        self.bsid = self.mysess.execute("select max(bsid) as 'bsmax' from qtsugar")
        self.spin_s = self.bsid.fetchone()
        self.ui.spinBsid.setValue(self.spin_s.bsmax)
        self.bpid = self.mysess.execute("select max(bpid) as 'bpmax' from vsigns_bp")
        self.spin_bp = self.bpid.fetchone()
        self.ui.spinBpid.setValue(self.spin_bp.bpmax)
        # started with 15 days but moving to 30 2-21-22
        # note to see if backuppc is working 2-27-22 8:31
        # 
        self.texbx = self.mysess.execute(
            "select foodid, fdate, fnotes from "
            + self.table_name
            + " where foodid = (select max(foodid) from "
            + self.table_name
            + " ) " )
        self.texbx_txt = self.texbx.fetchone()
        # ic(self.texbx_txt.foodid)
        self.ui.textEdit.setText(self.texbx_txt.fnotes)

        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("vsigns_bp")
        self.model.setFilter("bpid = (select max(bpid) from vsigns_bp)")
        self.model.select()

        self.tbl = self.ui.tblPrevRec
        self.tbl.setModel(self.model)

        ic(self.ok)
        ic(self.model.filter())
        ic(self.model.lastError().type())
        ic(self.model.lastError().text())
        ic(self.model.tableName())
        ic(self.model.select())
        # ic(self.db.connectionNames())
        # ic(self.db.tables())

    def update_rec(self):
        self.notes_dict = {
            "fdate": self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm"),
            "fnotes": self.ui.textEdit.toPlainText(),
            "sugarid": self.ui.spinBsid.value(),
            "bpid": self.ui.spinBpid.value(),
        }
        self.note_result = self.pg.pg_sql_notes_update(
            self.sqlite_conn, self.notes_dict, self.table_name, self.texbx_txt.foodid
        )
        if self.note_result:
            self.ui.lblRecord1.setText(
                f"SL up {self.table_name} {self.texbx_txt.foodid}"
            )
        if self.ui.chkPG.isChecked():
            # get maxes from postgresql foodid
            # check which table
            if self.table_name == "foodnotes":
                self.pg_table_name = "foodnotes"
            elif self.table_name == "fastnotes":
                self.pg_table_name = "fastnotes"
            else:
                self.pg_table_name = "foodnotes"
            ic(self.pg_table_name)
            self.pg_max_foodid = self.pg_sess.execute(
                "select foodid from "
                + self.pg_table_name
                + " where fdate = (select max(fdate) from "
                + self.pg_table_name
                + ")"
            )
            self.pg_foodid = self.pg_max_foodid.fetchone()
            self.pg_maxid = self.pg_foodid.foodid
            # bpid
            self.pg_max_bpid = self.pg_sess.execute(
                "select max(bpid) as maxbpid from vsigns_bp"
            )
            self.pg_bpid = self.pg_max_bpid.fetchone()
            self.pg_maxbpid = self.pg_bpid.maxbpid
            # bsid
            self.pg_max_bsid = self.pg_sess.execute(
                "select max(bsid) as maxbsid from qtsugar"
            )
            self.pg_bsid = self.pg_max_bsid.fetchone()
            self.pg_maxbsid = self.pg_bsid.maxbsid

            self.pg_notes_dict = {
                "fdate": self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm"),
                "fnotes": self.ui.textEdit.toPlainText(),
                "sugarid": self.pg_maxbsid,
                "bpid": self.pg_maxbpid,
            }

            self.pg_result = self.pg.pg_sql_notes_update(
                self.pg_conn, self.pg_notes_dict, self.pg_table_name, self.pg_maxid
            )
            if self.pg_result:
                self.ui.lblRecord2.setText(
                    f"PG up {self.pg_table_name} {self.pg_maxid}"
                )
                self.populate_boxes()
        else:
            self.populate_boxes()

    def add_rec(self):
        self.my_table = dbsql.table(
            self.table_name,
            dbsql.column("fdate"),
            dbsql.column("sugarid"),
            dbsql.column("bpid"),
            dbsql.column("fnotes"),
        )
        self.notes_dict = {
            "fdate": self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm"),
            "fnotes": self.ui.textEdit.toPlainText(),
            "sugarid": self.ui.spinBsid.value(),
            "bpid": self.ui.spinBpid.value(),
        }
        self.ins = self.my_table.insert().values(self.notes_dict)

        self.result = self.mysess.execute(self.ins)
        self.mysess.commit()
        if self.result:
            self.ui.lblRecord1.setText(f"SL Rec Add {self.table_name}")
        if self.ui.chkPG.isChecked():
            # bpid
            # get maxes from postgresql foodid
            # check which table
            if self.table_name == "foodnotes":
                self.pg_table_name = "foodnotes"
            elif self.table_name == "fastnotes":
                self.pg_table_name = "fastnotes"
            else:
                self.pg_table_name = "foodnotes"
            ic(self.pg_table_name)

            self.pg_max_bpid = self.pg_sess.execute(
                "select max(bpid) as maxbpid from vsigns_bp"
            )
            self.pg_bpid = self.pg_max_bpid.fetchone()
            self.pg_maxbpid = self.pg_bpid.maxbpid
            # bsid
            self.pg_max_bsid = self.pg_sess.execute(
                "select max(bsid) as maxbsid from qtsugar"
            )
            self.pg_bsid = self.pg_max_bsid.fetchone()
            self.pg_maxbsid = self.pg_bsid.maxbsid
            # make the dictionary
            self.pg_notes_dict = {
                "fdate": self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm"),
                "fnotes": self.ui.textEdit.toPlainText(),
                "sugarid": self.pg_maxbsid,
                "bpid": self.pg_maxbpid,
            }
            self.pg_result = self.pg.pg_sql_notes_insert(
                self.pg_conn, self.pg_notes_dict, self.pg_table_name
            )
            if self.pg_result:
                self.ui.lblRecord2.setText(f"PG add {self.pg_table_name}")
                self.populate_boxes
        else:
            self.populate_boxes()

    def exitfunc(self):
        self.db.close()
        self.model.database().close()
        if self.db.isOpen():
            self.db.removeDatabase(self.conn_name)
        ic(self.model.lastError().text())
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    if sys.argv.__len__() == 2:
        main = Main(sys.argv[0], sys.argv[1])
        main.show()
        sys.exit(app.exec_())
    else:
        main = Main(sys.argv[0])
        main.show()
        sys.exit(app.exec_())
