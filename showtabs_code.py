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
        self.fillTables()
    def fillTables(self):    
        self.conn_name = "tblshowqry"
        self.dbt = QSqlDatabase.addDatabase("QSQLITE", self.conn_name)
        self.dbt.setDatabaseName("/data/sqlite/vitals.db")
        self.ok = self.dbt.open()
        self.bpmodel = QSqlTableModel(db=self.dbt)
        self.bpmodel.setTable('vsigns_bp')
        self.bpfilter = "bpid >= ((select max(bpid) from vsigns_bp) - 16)"
        self.bpmodel.setFilter(self.bpfilter)
        self.bpmodel.setSort(0, Qt.DescendingOrder)
        self.ui.tblVbp.setModel(self.bpmodel)
        self.bpmodel.select()
        self.ui.tblVbp.setColumnHidden(0, True)
        self.ui.tblVbp.resizeColumnToContents(7)
        self.ui.tblVbp.resizeRowsToContents()
        self.ui.tblVbp.setColumnWidth(1, 160)
        ################################################
        # foodnotes
        self.foodmodel = QSqlTableModel(db=self.dbt)
        self.foodmodel.setTable('foodnotes')
        self.foodmodel.setFilter('foodid >= ((select max(foodid) from foodnotes) - 16)')
        self.foodmodel.setSort(0,Qt.DescendingOrder)
        self.ui.tblVfood.setModel(self.foodmodel)
        self.foodmodel.select()
        self.ui.tblVfood.setColumnHidden(0, True)
        self.ui.tblVfood.setColumnHidden(3, True)
        self.ui.tblVfood.setColumnHidden(4, True)
        self.ui.tblVfood.resizeColumnToContents(2)
        self.ui.tblVfood.resizeRowsToContents()
        self.ui.tblVfood.setColumnWidth(1, 160)
        #################################################
        self.fastmodel = QSqlTableModel(db=self.dbt)
        self.fastmodel.setTable('fastnotes')
        self.fastmodel.setFilter('foodid >= ((select max(foodid) from fastnotes) - 16)')
        self.fastmodel.setSort(0, Qt.DescendingOrder)
        self.ui.tblVfast.setModel(self.fastmodel)
        self.fastmodel.select()
        self.ui.tblVfast.setColumnHidden(0, True)
        self.ui.tblVfast.setColumnHidden(2, True)
        self.ui.tblVfast.setColumnHidden(3, True)
        self.ui.tblVfast.resizeColumnToContents(4)
        # self.ui.tblVfast.resizeRowsToContents()
        self.ui.tblVfast.setColumnWidth(1, 160)
        self.ui.actionExit.triggered.connect(self.myExit)
        # self.dbt.close()


    def closeDB(self):
        debug(self.dbt.isOpen())
        debug(self.dbt.lastError().text())
        debug(self.dbt.contains(self.conn_name))
        self.ui.tblVbp.setModel(None)
        self.ui.tblVfood.setModel(None)
        self.ui.tblVfast.setModel(None)
        del self.foodmodel
        del self.fastmodel
        del self.bpmodel
        # del self.dbt
        self.dbt.close()
        # self.dbt = None
        self.dbt.removeDatabase('tblshowqry')

        # QSqlDatabase.removeDatabase('tblshowqry')


        debug(self.dbt.lastError().text())

    def myExit(self):
        self.closeDB()
        self.close()


    # close connections on close window for no connection errors
def closeEvent(self):
    self.closeDB()
    self.close()

if __name__ == "__main__":
    # debug(__name__)
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
