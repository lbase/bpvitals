import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QDataWidgetMapper, QTableView
from PyQt5 import QtWidgets
from PyQt5.QtCore import QModelIndex, QDateTime, Qt, QVariant
from icecream import ic
from sugar import Ui_Sugar
import numpy as np


class Main(QtWidgets.QWidget, Ui_Sugar):
    def __init__(self, object, mytable="qtsugar"):
        super(Main, self).__init__()
        self.mytable = mytable
        self.ui = Ui_Sugar()
        self.ui.setupUi(self)
        self.conn_name = "sugcode"
        self.sdb = QSqlDatabase.addDatabase("QSQLITE", self.conn_name)
        self.sdb.setDatabaseName("/home/rfile/python3/bpvitals/vitals.db")
        ok = self.sdb.open()
        if ok:
            self.model = QSqlTableModel(db=self.sdb)
            self.model.setTable(mytable)
            self.model.setSort(0, Qt.AscendingOrder)
            self.model.setFilter("bsid = (select max(bsid) from qtsugar)")
            self.ui.tblViewRec.setModel(self.model)
            ic(self.model.tableName())
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
        self.sugarnp = np.arange(50, 200, 1)
        for i in self.sugarnp:
            self.ui.sugarCombo.addItem(str(i))
        self.now = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(self.now)
        self.ui.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.ui.btnInsert.clicked.connect(self.recinsert)
        self.ui.btnExit.clicked.connect(self.exitfunc)

    def recinsert(self):
        self.r = self.model.record()
        self.r.setValue(
            "bsdate", self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm")
        ),
        self.r.setValue("bsugar", self.ui.sugarCombo.currentText())
        self.r.setValue("comment", self.ui.txtComment.toPlainText())
        self.model.insertRecord(-1, self.r)
        self.model.submit()
        self.submit_OK = self.model.select()
        if self.submit_OK:
            self.ui.lblInsert.setText("Rec Inserted")

    def exitfunc(self):
        self.sdb.close()
        self.model.database().close()
        if self.sdb.isOpen():
            self.sdb.removeDatabase(self.conn_name)
        ic(self.model.lastError().text())
        self.close()


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
