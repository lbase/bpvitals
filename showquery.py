#!/usr/bin/env python3
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow
from icecream import ic
from devtools import debug
from forms.showquerywin import Ui_MainWindow
from vitals_code import Main as VMain
from graphs import modbpstats


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, table_name="vsigns_bp"):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connshow_name = "dbshowqry"
        self.db = QSqlDatabase.addDatabase("QSQLITE", self.connshow_name)
        self.db.setDatabaseName("/data/sqlite/vitals.db")
        ok = self.db.open()
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable(table_name)
        self.ui.tb1.setModel(self.model)
        self.model.setSort(0, Qt.DescendingOrder)
        self.model.setHeaderData(1, Qt.Horizontal ,"Date")
        self.model.setHeaderData(2, Qt.Horizontal ,"Systolic")
        self.model.setHeaderData(3, Qt.Horizontal ,"Diastolic")
        self.model.setHeaderData(4, Qt.Horizontal ,"HR")
        self.model.setHeaderData(5, Qt.Horizontal ,"Sugar")
        self.model.setHeaderData(6, Qt.Horizontal ,"Ketone")
        self.model.setHeaderData(7, Qt.Horizontal ,"Oxy")
        self.model.setHeaderData(8, Qt.Horizontal ,"Comment")
        
        # table sizing
        # self.ui.tb1.maximumViewportSize()
        # hide id
        self.ui.tb1.setColumnHidden(0,True)
        # change headers
        
        self.ui.tb1.resizeColumnsToContents()
        self.ui.tb1.setColumnWidth(1, 160)

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
        # os.system("/home/rfile/python3/bpvitals/bpstats.py")
        modbpstats.bp7days()

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
        debug(QSqlDatabase.connectionNames())
        self.db.close()
        self.ui.tb1.setModel(None)
        del self.model
        self.db.removeDatabase(self.connshow_name)
        # debug(self.model.lastError().text())
        debug(QSqlDatabase.connectionNames())
        self.close()


if __name__ == "__main__":
    # debug(__name__)
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
