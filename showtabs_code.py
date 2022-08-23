#! /usr/bin/env python3

import sys
#import sqlalchemy as dbsql
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from devtools import debug
#from sqlalchemy.orm import sessionmaker
#from utils.lclutils import Sqlpg
from forms.showtables import Ui_ShowTables
from graphs import modbpstats


class MainWindow(QMainWindow, Ui_ShowTables):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ShowTables()
        self.ui.setupUi(self)
        self.conn_name = "tblshowqry"
        self.db = QSqlDatabase.addDatabase("QSQLITE", self.conn_name)
        self.db.setDatabaseName("/data/sqlite/vitals.db")
        ok = self.db.open()
        self.bpmodel = QSqlTableModel(db=self.db)
        self.bpmodel.setTable('vsigns_bp')
        self.bpfilter = "bpid >= ((select max(bpid) from vsigns_bp) - 16)"
        self.bpmodel.setFilter(self.bpfilter)
        self.bpmodel.setSort(0, Qt.DescendingOrder)
        self.ui.tblVbp.setModel(self.bpmodel)
        self.bpmodel.select()

if __name__ == "__main__":
    # debug(__name__)
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
