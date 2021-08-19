#! /usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QDataWidgetMapper, QTableView
from PyQt5 import QtWidgets
from PyQt5.QtCore import QModelIndex, QDateTime, Qt, QVariant
from icecream import ic
from addvitals import Ui_Form
import sqlalchemy as dbsql


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
        self.db.setDatabaseName("/data/sqlite/vitals.db")

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

        self.ui.btnInsert.clicked.connect(self.recinsert)
        self.ui.btnExit.clicked.connect(self.exitfunc)
        self.ui.chkPG.setChecked(1)
        # self.ui.chkPG.stateChanged.connect(self.setup_pg)
        self.setup_pg()

    def recinsert(self):
        r = self.model.record()
        r.setValue(
            "bpdate", self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm"),
        )
        r.setValue("bpsys", self.ui.cmbsystolic.currentText())
        r.setValue("bpdia", self.ui.cmbdiastolic.currentText())
        r.setValue("bphr", self.ui.cmbheartrate.currentText())
        r.setValue("bpsugar", self.ui.cmbsugar.currentText())
        r.setValue("bpoxy", self.ui.cmboxy.currentText())
        r.setValue("bpcomment", self.ui.lncomment.toPlainText())
        self.model.insertRecord(-1, r)
        self.model.submit()
        ic(self.model.lastError().text())
        self.submit_OK = self.model.select()
        ic(self.model.submit())
        if self.submit_OK:
            self.ui.lblInsert.setText("Rec Inserted")
        if self.ui.chkPG.isChecked():
            # self.pg_table_name = self.table_name
            self.postgres_recinsert(self.mytable)

        # self.db.close()

    def setup_pg(self):
        if self.ui.chkPG.isChecked():
            self.eng = dbsql.create_engine("postgresql://rfile:simple@flatboy/rfile")
            self.conn = self.eng.connect()  # use this as connection for insert query

    def postgres_recinsert(self, pg_table_name):
        """[inserts record postgresql]
           {{tbname}}
        """
        # self.tbname = "vsigns_bp"  # vsigns_bp or vsigns_bloodpressure because columns match
        if self.ui.chkPG.isChecked():
            self.pg_table_name = pg_table_name
            self.pg_table_name = dbsql.table(
                self.pg_table_name,
                dbsql.column("bpdate"),
                dbsql.column("bpsys"),
                dbsql.column("bpdia"),
                dbsql.column("bphr"),
                dbsql.column("bpsugar"),
                dbsql.column("bpoxy"),
                dbsql.column("bpcomment"),
            )
            self.ins = self.pg_table_name.insert().values(
                {
                    "bpdate": self.ui.dateTimeEdit.dateTime().toString(),  # "bpdate" : self.dt,\
                    "bpsys": self.ui.cmbsystolic.currentText(),
                    "bpdia": self.ui.cmbdiastolic.currentText(),
                    "bphr": self.ui.cmbheartrate.currentText(),
                    "bpsugar": self.ui.cmbsugar.currentText(),
                    "bpoxy": self.ui.cmboxy.currentText(),
                    "bpcomment": self.ui.lncomment.toPlainText(),
                }
            )
            self.result = self.conn.execute(self.ins)
            if self.result:
                self.ui.lblInsert.setText(
                    "Rec Inserted PG:\n %s" % (self.pg_table_name)
                )

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
        main = Main(sys.argv[0], sys.argv[1])
        main.show()
        sys.exit(app.exec_())
    else:
        main = Main(sys.argv[0])
        main.show()
        sys.exit(app.exec_())
