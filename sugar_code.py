#! /usr/bin/env python3

import sys

import sqlalchemy as dbsql
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMessageBox
from icecream import ic
from devtools import debug
from sqlalchemy.orm import sessionmaker
# from utils.lclutils import Sqlpg
from forms.sugar import Ui_Sugar
# for graph
# import sugarstats48
#import sugarstats8days
from graphs import modbpstats


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
            self.bsidint = self.bsidint.strip("(),")
            # print(self.bsidint)
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
        self.ui.btnGraph_2.clicked.connect(self.bpgraph2)
        # Sunday, July 10, 2022 2:18:43 PM EDT rfile add for graphs
        

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






    def exitfunc(self):
        self.sdb.close()
        self.model.database().close()
        if self.sdb.isOpen():
            self.sdb.removeDatabase(self.conn_name)
        ic(self.model.lastError().text())
        
        self.close()
    def bpgraph(self):
       #os.system("/home/rfile/python3/bpvitals/bpstats.py")
       modbpstats.sugar48()
       
       
    def bpgraph2(self):
       modbpstats.days7()
       
    
       

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
