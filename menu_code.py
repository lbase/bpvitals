#! /usr/bin/env python3

import sys
import sqlalchemy as dbsql
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMessageBox, QApplication
from icecream import ic
from devtools import debug
from sqlalchemy.orm import sessionmaker
from utils.lclutils import Sqlpg
from forms.menu import Ui_Menu
from graphs import modbpstats
from vitals_code import Main as vitals
from showquery import MainWindow as queryWin
from weight_code import Main as Wtentry
from notes_code import Main as notes


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
        debug(self.sdb.databaseName())
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
        self.ui.sugarCombo.addItems(str(i) for i in range(50, 201, 1))
        self.ui.sugarCombo.setCurrentIndex(50)
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
        self.ui.chkPG.setChecked(1)
        # self.ui.chkPG.stateChanged.connect(self.setup_pg)
        self.setup_pg()
        # Sunday, July 10, 2022 2:18:43 PM EDT rfile add for graphs
    def fillsugartab(self):
        # get number for max(bsid)
        self.eng = dbsql.create_engine("sqlite:////data/sqlite/vitals.db")
        self.mysession = sessionmaker(bind=self.eng)
        self.mysess = self.mysession()
        self.bsid = self.mysess.execute("select max(bsid) as 'bsmax' from qtsugar")
        self.bsidval = self.bsid.fetchone()
        self.bsidint = str(self.bsidval)
        self.bsidint = self.bsidint.strip("(),")
        # print(self.bsidint)
        self.bsidint = int(self.bsidint)
        self.bsid_20 = (self.bsidint - 20)

        # end get number
        self.model = QSqlTableModel(db=self.sdb)
        self.model.setTable(self.mytable)
        self.model.setSort(0, Qt.DescendingOrder)
        self.model.setFilter("bsid >= " + str(self.bsid_20))
        # self.model.setFilter("bsid = (select max(bsid) from qtsugar)")
        self.ui.tblViewRec.setModel(self.model)
        self.ui.tblViewRec.maximumViewportSize()
        self.ui.tblViewRec.resizeColumnsToContents()
        self.ui.tblViewRec.setColumnWidth(1, 160)
        # debug(self.model.tableName())
        self.model.select()
        msg = f"mytable: {self.mytable}"
        self.message(msg)

    def recinsert(self):
        self.r = self.model.record()
        self.r.setValue(
            "bsdate", self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm")
        ),
        self.r.setValue("bsugar", self.ui.sugarCombo.currentText())
        self.r.setValue("comment", self.ui.txtComment.toPlainText())
        self.submit_OK = self.model.insertRecord(-1, self.r)
        self.model.submit()
        self.model.select()
        if self.submit_OK:
            self.ui.lblInsert.setText("Rec Inserted")
            self.message("Record inserted from menu_code")


        if self.ui.chkPG.isChecked():
            self.postgres_recinsert(self.mytable)
        else:
            return

    def setup_pg(self):
        self.pg = Sqlpg()
        self.pg_conn = self.pg.pg_sql_connect()
        if not self.pg_conn:
            dbDlg = QMessageBox(self)
            dbDlg.setWindowTitle("Database error")
            dbDlg.setText(
                "Database did not connect \n"
                + self.eng.driver()
                + " \n"
                + self.eng.lastError().text()
            )
            dbDlg.exec()

    def postgres_recinsert(self, pg_table_name):
        """[inserts record postgresql]
           {{tbname}}
        """
        if self.ui.chkPG.isChecked():
            # self.tbname = "vsigns_bp"  # vsigns_bp or vsigns_bloodpressure because columns match
            self.pg_table_name = pg_table_name
            self.sugar_dict = {
                "bsdate": self.ui.dateTimeEdit.dateTime().toString(),  # "bpdate" : self.dt,\
                "bsugar": self.ui.sugarCombo.currentText(),
                "comment": self.ui.txtComment.toPlainText(),
            }
            self.result = self.pg.pg_sql_qtsugar_insert(
                self.pg_conn, self.sugar_dict, self.pg_table_name
            )

            if self.result:
                self.ui.lblInsert.setText(
                    "Rec Inserted PG:\n %s" % (self.pg_table_name)
                )

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
        self.message(f'graph 48 {self.mytable} ')
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
        self.showwt = Wtentry('fatty')
        self.showwt.show()

    def foodnotes(self):
        self.notes = notes(self, "foodnotes")
        self.notes.show()



    def fastnotes(self):
        self.fnotes = notes(self, "fastnotes")
        self.fnotes.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main(sys.argv)
    window.show()
    app.exec_()
else:

    main = Main(sys.argv)
    main.show()
    sys.exit(app.exec_())
