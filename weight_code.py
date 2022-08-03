#! /usr/bin/env python3
# taken from vitals_code
import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import QtWidgets , QtGui
from PyQt5.QtCore import  QDateTime, Qt, QSettings
from icecream import ic
from weight import Ui_Weight as Wform
from lclutils import Sqlpg
import modbpstats


class Main(QtWidgets.QWidget, Wform):
    def __init__(self):
        super(Main, self).__init__()
        # build ui
        self.mytable = "fatty"
        self.ui = Wform()
        self.ui.setupUi(self)
        self.conn_name = "wcode"
        self.db = QSqlDatabase.addDatabase("QSQLITE", self.conn_name)
        self.db.setDatabaseName("/data/sqlite/vitals.db")

        ok = self.db.open()
        if ok:
            self.model = QSqlTableModel(db=self.db)
            self.model.setTable(self.mytable)
            self.model.setSort(0, Qt.AscendingOrder)
            self.model.select()
            # self.db.close()   # going to open close in  recinsert
        else:
            dbDlg = QMessageBox(self)
            dbDlg.setWindowTitle("Database error")
            dbDlg.setText(
                "Database did not connect \n"
                + self.db.driverName()
                + " \n"
                + self.db.lastError().text()
            )
            dbDlg.exec()
            sys.exit()
    # ---------------------------------------------------------------------------- #
    #                                start of setup                                #
    # ---------------------------------------------------------------------------- #
        # self.ui.setWindowTitle(mytable)
        now = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(now)
        self.ui.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.ui.cmbWeight.setValidator(QtGui.QDoubleValidator(0.0,300.0,1,notation=QtGui.QDoubleValidator.StandardNotation))

        self.ui.btnSubmit.clicked.connect(self.recinsert)


    def recinsert(self):
        r = self.model.record()
        r.setValue("ftime", self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm"))
        r.setValue("weight", int(self.ui.cmbWeight.currentText()))
        r.setValue("bmi", int(self.ui.cmbBmi.currentText()))
        self.model.insertRecord(-1, r)
        self.model.submit()
        ic(self.model.lastError().text())
        self.submit_OK = self.model.select()
        ic(self.model.submit())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
