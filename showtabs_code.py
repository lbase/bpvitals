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
        self.ui.tblVbp.setColumnHidden(0, True)
        self.ui.tblVbp.resizeColumnToContents(7)
        self.ui.tblVbp.setColumnWidth(1, 160)
        ################################################
        # foodnotes
        self.foodmodel = QSqlTableModel(db=self.db)
        self.foodmodel.setTable('foodnotes')
        self.foodmodel.setFilter('foodid >= ((select max(foodid) from foodnotes) - 16)')
        self.foodmodel.setSort(0,Qt.DescendingOrder)
        self.ui.tblVfood.setModel(self.foodmodel)
        self.foodmodel.select()
        self.ui.tblVfood.setColumnHidden(0, True)
        self.ui.tblVfood.setColumnHidden(3, True)
        self.ui.tblVfood.setColumnHidden(4, True)
        self.ui.tblVfood.resizeColumnToContents(2)
        self.ui.tblVfood.setColumnWidth(1, 160)
        #################################################
        self.fastmodel = QSqlTableModel(db=self.db)
        self.fastmodel.setTable('foodnotes')
        self.fastmodel.setFilter('foodid >= ((select max(foodid) from fastnotes) - 16)')
        self.fastmodel.setSort(0, Qt.DescendingOrder)
        self.ui.tblVfast.setModel(self.fastmodel)
        self.fastmodel.select()
        self.ui.tblVfast.setColumnHidden(0, True)
        self.ui.tblVfast.setColumnHidden(3, True)
        self.ui.tblVfast.setColumnHidden(4, True)
        self.ui.tblVfast.resizeColumnToContents(2)
        self.ui.tblVfast.setColumnWidth(1, 160)


if __name__ == "__main__":
    # debug(__name__)
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
