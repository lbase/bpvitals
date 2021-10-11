#!/usr/bin/env python3
import sys
import os
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5.QtCore import QCoreApplication
from icecream import ic
from icecream.icecream import IceCreamDebugger
from showquerywin import Ui_MainWindow
from vitals_code import Main as VMain


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, table_name="vsigns_bp"):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn_name = "dbshowqry"
        self.db = QSqlDatabase.addDatabase("QSQLITE", self.conn_name)
        self.db.setDatabaseName("/data/sqlite/vitals.db")
        ok = self.db.open()
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable(table_name)
        self.ui.tb1.setModel(self.model)
        self.model.setSort(0, Qt.DescendingOrder)
        # self.model.setFilter("bpcomment like '%fast%'")
        self.model.select()
        self.ui.btnVform.clicked.connect(self.add_new)
        self.ui.btnRefresh.clicked.connect(self.refreshrecs)
        self.ui.actionExit.triggered.connect(self.exitFunc)
        self.ui.btnGraphbp.clicked.connect(self.bpgraph)
        self.ui.btnDelete.clicked.connect(self.delrows)
        self.setWindowTitle(table_name)
        self.showSbar("Setup Complete")

    def show_vmain(self):
        if "vform" in self.__dict__:
            self.vform.window.close()
            self.vform = None
            self.showSbar("Vitals form closed")

        else:
            self.vform = VMain()
            self.vform.show()
            self.showSbar("Vitals form open")

    def add_new(self):
        self.model.insertRow(0)

    def refreshrecs(self):
        self.model.select()
        self.ui.tb1.reset()

    def bpgraph(self):
        self.showSbar("showing graphs")
        os.system("/home/rfile/python3/bpvitals/bpstats.py")

    def showSbar(self, msg):
        self.ui.statusbar.showMessage(msg)

    def delrows(self):
        self.showSbar("remove highlighted rows")
        l = self.ui.tb1.selectedIndexes()
        if not len(l):
            return
        else:
            self.showSbar(str(len(l) / 8) + " rows selected")
        rows = set([i.row() for i in l])
        rows = list(rows)
        rows.sort()
        first = rows[0]
        count = len(rows)
        self.model.removeRows(first, count)
        self.model.submitAll()

    def exitFunc(self):
        self.db.close()
        ic(self.model.lastError().text())
        self.close()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()

