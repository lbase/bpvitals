#! /usr/bin/env python3
import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import QtWidgets
from PyQt5.QtCore import  QDateTime, Qt, QSettings
from icecream import ic
from devtools import debug
from forms.addvitals import Ui_Form
# from utils.lclutils import Sqlpg
from graphs import modbpstats
import numpy as np



class Main(QtWidgets.QWidget, Ui_Form):
    def __init__(self, mytable="vsigns_bp"):
    #def __init__(self, object, mytable="vsigns_bp"):
        super(Main, self).__init__()
        # build ui
        self.mytable = mytable
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.conn_name = "vcode"
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
        self.setWindowTitle(mytable)

        self.ui.cmbsystolic.addItems(str(i) for i in range(120, 141, 1))
        self.ui.cmbdiastolic.addItems(str(j) for j in range(75, 101, 1))
        self.ui.cmbheartrate.addItems(str(k) for k in range(60, 91, 1))
        self.ui.cmbheartrate.setCurrentIndex(20)
        self.ui.cmbsugar.addItems(str(l) for l in range(75, 141, 1))
        self.ui.cmbsugar.setCurrentIndex(10)
        oxyitems = ["96", "97"]
        self.ui.cmboxy.addItems(oxyitems)
        now = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(now)
        self.ui.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm")
        # add ketone
        ketoneval = np.linspace(0,4,44)
        # debug(ketoneval)
        self.ui.cmbketone.addItems(str(round(k,1)) for k in ketoneval)
        self.ui.cmbketone.setCurrentText("0.01")

        self.ui.btnInsert.clicked.connect(self.recinsert)
        self.ui.btnExit.clicked.connect(self.exitfunc)
        self.ui.btnbpgraph.clicked.connect(self.bpgraph)
        self.ui.btnsugar8.clicked.connect(self.sug8graph)
        self.ui.btnsugar48.clicked.connect(self.sug48graph)

    def recinsert(self):
        r = self.model.record()
        r.setValue(
            "bpdate", self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm"),
        )
        r.setValue("bpsys", self.ui.cmbsystolic.currentText())
        r.setValue("bpdia", self.ui.cmbdiastolic.currentText())
        r.setValue("bphr", self.ui.cmbheartrate.currentText())
        r.setValue("bpsugar", self.ui.cmbsugar.currentText())
        r.setValue("ketone", float(self.ui.cmbketone.currentText()))
        r.setValue("bpoxy", self.ui.cmboxy.currentText())
        r.setValue("bpcomment", self.ui.lncomment.toPlainText())
        self.model.insertRecord(-1, r)
        self.model.submit()
        self.ui.txt_msg.setPlainText(ic(self.model.lastError().text()))
        self.submit_OK = self.model.select()
        debug(self.model.submit())
        self.ui.txt_msg.setPlainText(self.ui.txt_msg.toPlainText() + "record should be inserted")
        if self.submit_OK:
            self.ui.lblInsert.setText("Rec Inserted")


        # self.db.close()
    def bpgraph(self):
        modbpstats.bp7days()

    def sug8graph(self):
        modbpstats.days7()

    def sug48graph(self):
        modbpstats.sugar48()


    def refresh(self):
        self.model.select()

    def write_settings(self):
        settings = QSettings("bpvitals", "vitals")
        settings.setValue("tablename", self.mytable)
        settings.setValue("databasename", self.db.databaseName())


    def closeDatabase(self):
            del self.model
            self.db.close()
            del self.db
            QSqlDatabase.removeDatabase(self.conn_name)


    def exitfunc(self):
        # self.write_settings()
        self.closeDatabase()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    if sys.argv.__len__() == 2:
        main = Main([sys.argv])
        main.show()
        sys.exit(app.exec_())
        ic(sys.argv.__len__())
    else:
        main = Main()
        main.show()
        sys.exit(app.exec_())
