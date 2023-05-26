#! /usr/bin/env python3
# taken from vitals_code
import sys
import logging
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import QtWidgets
from PyQt5.QtCore import  QDateTime, Qt
from icecream import ic
from forms.weight import Ui_Weight as Wform
from graphs import modbpstats


class Main(QtWidgets.QWidget, Wform):
    def __init__(self, mytable="qfatty"): # qfatty is regular table - fatty is for test - has same structure
        super(Main, self).__init__()
        # build ui
        self.mytable = mytable
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
            self.message(f"table name: {self.mytable}")
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
        # self.ui.cmbWeight.setValidator(QtGui.QDoubleValidator(0.0,300.0,1,notation=QtGui.QDoubleValidator.StandardNotation))

        self.ui.btnSubmit.clicked.connect(self.recinsert)
        self.ui.btnWeightchart.clicked.connect(self.weightchart)
        self.ui.btnExit.clicked.connect(self.exitfunc)

    def recinsert(self):
        try:
            r = self.model.record()
            r.setValue("ftime", self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm"))
            r.setValue("weight", float(self.ui.spnWeight.text()))
            r.setValue("bmi", float(self.ui.spnBmi.text()))
            r.setValue("body_fat", float(self.ui.spnBodyfat.text()))
            r.setValue("fat_free_body_weight", float(self.ui.spnFatfree.text()))
            r.setValue("subcutaneous_fat", float(self.ui.spnSubfat.text()))
            r.setValue("visceral_fat", float(self.ui.spnViscfat.text()))
            r.setValue("body_water", float(self.ui.spnWater.text()))
            r.setValue("muscle_mass", float(self.ui.spnMuscle.text()))
            r.setValue("skeletal_muscles", float(self.ui.spnSkelmuscle.text()))
            r.setValue("bone_mass", float(self.ui.spnBonemass.text()))
            r.setValue("protein", float(self.ui.spnProtein.text()))
            r.setValue("bmr", float(self.ui.spnBmr.text()))
            r.setValue("metabolic_age", float(self.ui.spnAge.text()))
            self.model.insertRecord(-1, r)
            self.model.submit()

            self.submit_OK = self.model.select()
            self.message(f"record added; submit value: {self.submit_OK}  errors:  {self.model.lastError().text()}")
            self.logsingle()
        except:
            print(f"please check inputs are in range {self.model.lastError().text()} ")

    def logsingle(self):
        # log
        logger = logging.getLogger("dev")
        logger.setLevel(logging.INFO)
        fileHandler = logging.FileHandler("/data/sqlite/weight_lite.log")
        fileHandler.setLevel(logging.INFO)
        logger.addHandler(fileHandler)
        formatter = logging.Formatter(
            "%(asctime)s  %(name)s  %(levelname)s: %(message)s"
        )
        fileHandler.setFormatter(formatter)
        datestr = self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm")
        #datestr = self.ui.dateTimeEdit.dateTime()
        logger.info(f"single entry : {datestr} ")
        # log


    def weightchart(self):
        modbpstats.weightline()



    def message(self, s):
        self.ui.txtMsgbox.appendPlainText(s)

    def closeEvent(self, event):
        print('close event func triggered')
        self.exitfunc()


    def exitfunc(self):
        print('exitfunc')
        self.db.close()
        self.model.database().close()
        self.db.removeDatabase(self.conn_name)
        ic(self.model.lastError().text())
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    if sys.argv.__len__() == 2:
        main = Main(sys.argv[1])
        main.show()
        sys.exit(app.exec_())
    else:
        main = Main()
        main.show()
        sys.exit(app.exec_())
