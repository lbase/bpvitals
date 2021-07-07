import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QDataWidgetMapper, QTableView
from PyQt5 import QtWidgets
from PyQt5.QtCore import QModelIndex, QDateTime, Qt, QVariant
from icecream import ic
from addvitals import Ui_Form

import numpy as np


class Main(QtWidgets.QWidget, Ui_Form):
    def __init__(self, object, mytable="vsigns_bp"):
        ic(mytable)
        super(Main, self).__init__()
        # build ui
        self.mytable = mytable
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.conn_name = "vcode"
        self.db = QSqlDatabase.addDatabase("QSQLITE", self.conn_name)
        self.db.setDatabaseName("/home/rfile/python3/bpvitals/vitals.db")
        ok = self.db.open()
        if ok:
            self.model = QSqlTableModel(db=self.db)
            self.model.setTable(mytable)
            self.model.setSort(0, Qt.AscendingOrder)
            ic(self.model.tableName())
            self.model.select()
            # self.db.close()   # going to open close in  recinsert
        else:
            dbDlg = QMessageBox(self)
            dbDlg.setWindowTitle("Database error")
            dbDlg.setText("Database did not connect \n" +
                          self.db.driverName() + " \n" + self.db.lastError().text())
            dbDlg.exec()
            sys.exit()

        sysnp = np.arange(120, 149, 1)
        for i in sysnp:
            self.ui.cmbsystolic.addItem(str(i))
        dianp = np.arange(75, 100, 1)
        for j in dianp:
            self.ui.cmbdiastolic.addItem(str(j))
        pulsenp = np.arange(60, 90, 1)
        for k in pulsenp:
            self.ui.cmbheartrate.addItem(str(k))
        sugarnp = np.arange(75, 140, 1)
        for l in sugarnp:
            self.ui.cmbsugar.addItem(str(l))
        oxyitems = ["96", "97"]
        self.ui.cmboxy.addItems(oxyitems)
        now = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(now)

        self.ui.btnInsert.clicked.connect(self.recinsert)
        self.ui.btnExit.clicked.connect(self.exitfunc)
        # self.ui.btnRefresh.clicked.connect(self.setupdb)
        # self.ui.btnInsert.clicked.connect(self.mapper.submit)

    def recinsert(self):
        
        #r.setValue("bpid", myrow)
        # r.setValue("bpid", "DEFAULT")
        # r.setValue("bpdate" , QDateTime.currentDateTime())
        r = self.model.record() 
        r.setValue("bpdate", self.ui.dateTimeEdit.dateTime())
        r.setValue("bpsys", self.ui.cmbsystolic.currentText())
        r.setValue("bpdia", self.ui.cmbdiastolic.currentText())
        r.setValue("bphr", self.ui.cmbheartrate.currentText())
        r.setValue("bpsugar", self.ui.cmbsugar.currentText())
        r.setValue("bpoxy", self.ui.cmboxy.currentText())
        r.setValue("bpcomment", self.ui.lncomment.toPlainText())
        self.model.insertRecord(-1, r)
        self.model.submit()
        ic(self.model.lastError().text())
        self.model.select()
        ic(self.model.submit())
        # self.db.close()

    def refresh(self):
        self.model.select()

    def exitfunc(self):
        self.db.close()
        self.model.database().close()
        if self.db.isOpen():
            self.db.removeDatabase(self.conn_name)
        ic(self.model.lastError().text())
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    if sys.argv.__len__() == 2:
        main = Main(sys.argv[0],sys.argv[1])
        main.show()
        sys.exit(app.exec_())
    else:
        main = Main(sys.argv[0])
        main.show()
        sys.exit(app.exec_())
