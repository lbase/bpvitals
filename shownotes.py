#! /usr/bin/env python3
import sys
import os
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QApplication, QMainWindow
from icecream import ic
from devtools import debug
from forms.shownoteswin import Ui_NotesWin
from vitals_code import Main as VMain


class MainWindow(QMainWindow, Ui_NotesWin):
    def __init__(self, table_name="foodnotes"):
        self.table_name = table_name
        super().__init__()
        self.ui = Ui_NotesWin()
        self.ui.setupUi(self)
        self.conn_name = "dbshownotes"
        self.db = QSqlDatabase.addDatabase("QSQLITE", self.conn_name)
        self.db.setDatabaseName("/data/sqlite/vitals.db")
        ok = self.db.open()
        self.query = QSqlQuery(self.db)
        self.query.prepare(
            "select fdate, fnotes from "
            + self.table_name
            + " where fdate > (select date((select max(fdate)), '-30 day' ) from "
            + self.table_name
            + ") ORDER by fdate desc"
        )
        self.query.exec_()
        self.model = QSqlQueryModel()
        self.model.setQuery(self.query)
        self.ui.tb1.setModel(self.model)
        self.ui.tb1.resizeColumnsToContents()
        self.ui.tb1.resizeRowsToContents()
        self.ui.actionExit.triggered.connect(self.exitFunc)
        self.ui.btnGraphbp.clicked.connect(self.bpgraph)
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
        os.system("/utils/bpstats.py")

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

    def exitFunc(self, event):
        debug(QSqlDatabase.connectionNames())
        self.db.close()
        ic(self.model.lastError().text())
        self.close()


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()
# app.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if sys.argv.__len__() > 1:
        main = MainWindow(sys.argv[1])
        main.show()
        sys.exit(app.exec_())
    else:
        main = MainWindow()
        main.show()
        sys.exit(app.exec_())
