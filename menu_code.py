#! /home/rfile/.local/share/virtualenvs/bpvitals-z9m9Wh3n/bin/python3

# /usr/bin/env python3

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMessageBox, QApplication
from devtools import debug
# from networkx import double_edge_swap
from forms.menu import Ui_Menu
from graphs import modbpstats
from vitals_code import Main as vitals
from showquery import MainWindow as queryWin
from weight_code import Main as Wtentry
from notes_qtcode import Main as notes
from showtabs_code import MainWindow as showtabs
import numpy as np


class Main(QtWidgets.QWidget, Ui_Menu):
    def __init__(self, object, mytable="qtsugar"):
        super(Main, self).__init__()
        self.mytable = mytable
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.conn_name = "sugcode"
        self.sdb = QSqlDatabase.addDatabase("QSQLITE", self.conn_name)
        self.sdb.setDatabaseName("/data/sqlite/vitals.db")
        ok = self.sdb.open()
        # debug(self.sdb.databaseName())
        if ok:
            self.fillsugartab()

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
        self.ui.sugarCombo.addItems(str(i) for i in range(50, 301, 1))
        self.ui.sugarCombo.setCurrentIndex(50)
        ketoneval = np.linspace(0, 4, 44)
        # debug(ketoneval)
        self.ui.ketonecombo.addItems(str(round(k, 1)) for k in ketoneval)
        # self.ui.ketonecombo.addItems(str(k) for k in range(1, 4, 1))
        self.ui.ketonecombo.setCurrentText("0.01")
        # self.ui.ketonecombo.currentIndex(0)
        self.now = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(self.now)
        self.ui.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.ui.btnInsert.clicked.connect(self.recinsert)
        self.ui.btnExit.clicked.connect(self.exitfunc)
        self.ui.btnGraph48.clicked.connect(self.bpgraph48)
        self.ui.btnGraph8.clicked.connect(self.bpgraph8)
        self.ui.btnVitals.clicked.connect(self.vitals)
        self.ui.btnShowBP.clicked.connect(self.showbp)
        self.ui.btnRefresh.clicked.connect(self.fillsugartab)
        self.ui.btnWeight.clicked.connect(self.weightchart)
        self.ui.btnWeightshow.clicked.connect(self.weightentry)
        self.ui.btnFoodnotes.clicked.connect(self.foodnotes)
        self.ui.btnFastnotes.clicked.connect(self.fastnotes)
        self.ui.btnShowtabs.clicked.connect(self.showtabs)
        # Sunday, July 10, 2022 2:18:43 PM EDT rfile add for graphs

    def fillsugartab(self):
        self.model = QSqlTableModel(db=self.sdb)
        self.model.setTable(self.mytable)
        self.model.setSort(0, Qt.DescendingOrder)
        self.model.setFilter("bsid >= ((select max(bsid) from qtsugar) - 20)")
        self.ui.tblViewRec.setModel(self.model)
        self.ui.tblViewRec.maximumViewportSize()
        self.ui.tblViewRec.setColumnHidden(0, True)
        self.ui.tblViewRec.resizeColumnsToContents()
        self.ui.tblViewRec.setColumnWidth(1, 160)
        # debug(self.model.tableName())
        self.model.select()
        msg = f"mytable: {self.mytable} connections: {QSqlDatabase.connectionNames()}"
        self.message(msg)

    def recinsert(self):
        self.r = self.model.record()
        (
            self.r.setValue(
                "bsdate", self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm")
            ),
        )
        self.r.setValue("bsugar", self.ui.sugarCombo.currentText())
        self.r.setValue("comment", self.ui.txtComment.toPlainText())
        # ketone
        self.r.setValue("ketone", float(self.ui.ketonecombo.currentText()))
        self.submit_OK = self.model.insertRecord(-1, self.r)
        self.model.submit()
        self.model.select()
        if self.submit_OK:
            self.ui.lblInsert.setText("Rec Inserted")
            self.message("Record inserted from menu_code")

    def exitfunc(self):
        self.sdb.close()
        self.model.database().close()
        if self.sdb.isOpen():
            self.sdb.removeDatabase(self.conn_name)
        self.close()

    #############################################################################
    def message(self, s):
        self.ui.txtMsgs.appendPlainText(s)

        ##############################################################################

    def bpgraph48(self):
        self.message(f"graph 48 {self.mytable} ")
        modbpstats.sugar48()

    def bpgraph8(self):
        modbpstats.days7()

    def vitals(self):
        self.message("running vitals")
        self.vitals = vitals()
        self.vitals.show()

    def showbp(self):
        self.showqry = queryWin()
        self.showqry.show()

    def weightchart(self):
        modbpstats.weightline()

    def weightentry(self):
        self.showwt = Wtentry("qfatty")  # fatty test table qfatty regular table
        self.showwt.show()
        msg = f"mytable: {self.mytable} connections: {QSqlDatabase.connectionNames()}"
        self.message(msg)

    def foodnotes(self):
        self.notes = notes(self, "foodnotes")
        self.notes.show()
        msg = f"mytable: {self.mytable} connections: {QSqlDatabase.connectionNames()}"
        self.message(msg)

    def fastnotes(self):
        self.fnotes = notes(self, "fastnotes")
        self.fnotes.show()

    def showtabs(self):
        self.showtabs = showtabs()
        self.showtabs.show()
        msg = f"mytable: {self.mytable} connections: {QSqlDatabase.connectionNames()}"
        self.message(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main(sys.argv)
    window.show()
    app.exec_()
else:
    main = Main(sys.argv)
    main.show()
    sys.exit(app.exec_())
    