#! /usr/bin/env python3

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QDataWidgetMapper, QTableView
from PyQt5 import QtWidgets
from PyQt5.QtCore import QModelIndex, QDateTime, Qt, QVariant
from icecream import ic
from sugar import Ui_Sugar
import sqlalchemy as dbsql
from sqlalchemy.orm import sessionmaker
from lclutils import Sqlpg


class Main(QtWidgets.QWidget, Ui_Sugar):
    def __init__(self, object, mytable="qtsugar"):
        super(Main, self).__init__()
        self.mytable = mytable
        self.ui = Ui_Sugar()
        self.ui.setupUi(self)
        self.conn_name = "sugcode"
        self.sdb = QSqlDatabase.addDatabase("QSQLITE", self.conn_name)
        self.sdb.setDatabaseName("/data/sqlite/vitals.db")
        ok = self.sdb.open()
        if ok:
            # get number for max(bsid)
            self.eng = dbsql.create_engine("sqlite:////data/sqlite/vitals.db")
            self.mysession = sessionmaker(bind=self.eng)
            self.mysess = self.mysession()
            self.bsid = self.mysess.execute("select max(bsid) as 'bsmax' from qtsugar")
            self.bsidval = self.bsid.fetchone()
            self.bsidint = str(self.bsidval)
            self.bsidint = self.bsidint.strip("\(\)\,")
            self.bsidint = int(self.bsidint)
            self.bsid_20 = (self.bsidint - 20)

            # end get number
            self.model = QSqlTableModel(db=self.sdb)
            self.model.setTable(mytable)
            self.model.setSort(0, Qt.DescendingOrder)
            self.model.setFilter("bsid >= " + str(self.bsid_20) )
            # self.model.setFilter("bsid = (select max(bsid) from qtsugar)")
            self.ui.tblViewRec.setModel(self.model)
            self.ui.tblViewRec.maximumViewportSize()
            self.ui.tblViewRec.resizeColumnsToContents()
            self.ui.tblViewRec.setColumnWidth(1,160)
            # ic(self.model.tableName())
            self.model.select()

        else:
            dbDlg = QMessageBox(self)
            dbDlg.setWindowTitle("Database error")
            dbDlg.setText(
                "Database did not connect \n"
                + self.sdb.driverName()
                + " \n"
                + self.sdb.lastError().text()
            )
            dbDlg.exec()
            sys.exit()
            # ======================================================== #
            # ======================= ui setup ======================= #
            # ======================================================== #
        self.setWindowTitle(self.mytable)
        self.ui.sugarCombo.addItems(str(i) for i in range(50, 201, 1))
        self.ui.sugarCombo.setCurrentIndex(50)
        self.now = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(self.now)
        self.ui.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.ui.btnInsert.clicked.connect(self.recinsert)
        self.ui.btnExit.clicked.connect(self.exitfunc)
        self.ui.btnGraph.clicked.connect(self.bpgraph)
        self.ui.chkPG.setChecked(1)
        # self.ui.chkPG.stateChanged.connect(self.setup_pg)
        self.setup_pg()

    def recinsert(self):
        self.r = self.model.record()

        self.r.setValue(
            "bsdate", self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm")
        ),
        self.r.setValue("bsugar", self.ui.sugarCombo.currentText())
        self.r.setValue("comment", self.ui.txtComment.toPlainText())
        self.submit_OK = self.model.insertRecord(-1, self.r)
        self.model.submit()
        self.model.select()
        if self.submit_OK:
            self.ui.lblInsert.setText("Rec Inserted")

        if self.ui.chkPG.isChecked():
            self.postgres_recinsert(self.mytable)
        else:
            return

    def setup_pg(self):
        self.pg = Sqlpg()
        self.pg_conn = self.pg.pg_sql_connect()
        if not self.pg_conn:
            dbDlg = QMessageBox(self)
            dbDlg.setWindowTitle("Database error")
            dbDlg.setText(
                "Database did not connect \n"
                + self.eng.driver()
                + " \n"
                + self.eng.lastError().text()
            )
            dbDlg.exec()

    def postgres_recinsert(self, pg_table_name):
        """[inserts record postgresql]
           {{tbname}}
        """
        if self.ui.chkPG.isChecked():
            # self.tbname = "vsigns_bp"  # vsigns_bp or vsigns_bloodpressure because columns match
            self.pg_table_name = pg_table_name
            self.sugar_dict = {
                "bsdate": self.ui.dateTimeEdit.dateTime().toString(),  # "bpdate" : self.dt,\
                "bsugar": self.ui.sugarCombo.currentText(),
                "comment": self.ui.txtComment.toPlainText(),
            }
            self.result = self.pg.pg_sql_qtsugar_insert(
                self.pg_conn, self.sugar_dict, self.pg_table_name
            )

            if self.result:
                self.ui.lblInsert.setText(
                    "Rec Inserted PG:\n %s" % (self.pg_table_name)
                )

    def exitfunc(self):
        self.sdb.close()
        self.model.database().close()
        if self.sdb.isOpen():
            self.sdb.removeDatabase(self.conn_name)
        ic(self.model.lastError().text())
        self.close()
    def bpgraph(self):
        os.system("/home/rfile/python3/bpvitals/bpstats.py")

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