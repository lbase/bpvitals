#! /usr/bin/env python3


from forms.notes import Ui_Comment
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from devtools import debug
import sys


class Main(QtWidgets.QWidget, Ui_Comment):
    """docstring for Main
"""


    def __init__(self, object,  table_name="foodnotes"):
        # foodnotes default table alternate is fastnotes
        super(Main, self).__init__()
        self.table_name = table_name
        self.ui = Ui_Comment()
        self.ui.setupUi(self)

        # ---------------------------------------------------------------- #
        #            database connection                                   #
        # ---------------------------------------------------------------- #
        # https://realpython.com/python-pyqt-database/#running-sql-queries-with-pyqt
        # queries
        self.conn_name = "notes"
        self.dbnotes = QSqlDatabase.addDatabase("QSQLITE", self.conn_name)
        self.dbnotes.setDatabaseName("/data/sqlite/vitals.db")
        self.okdbnotes = self.dbnotes.open()
        debug(self.okdbnotes)
        ### table
        self.conn_rec = "bprec"
        self.db = QSqlDatabase.addDatabase("QSQLITE", self.conn_rec)
        self.db.setDatabaseName("/data/sqlite/vitals.db")
        self.ok = self.db.open()
        #debug(self.ok)


        # ---------------------------------------------------------------------------- #
        #              table name in window title so I can tell what table              #
        # ---------------------------------------------------------------------------- #
        self.setWindowTitle(self.table_name)
        # current date
        now = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(now)
        # buttons
        self.ui.btnAdd.clicked.connect(self.add_rec)
        self.ui.btnUpdate.clicked.connect(self.update_rec)
        self.ui.btnExit.clicked.connect(self.exitfunc)
        self.populate_boxes()
        # ---------------------------------------------------------------------------- #
        #                      get numbers and one previous record                     #
        # ---------------------------------------------------------------------------- #

    def populate_boxes(self):
        ####

        # self.query = QSqlQuery()
        ####
        self.query = "select max(bsid) as bsmax from qtsugar"
        self.bsid = QSqlQuery(self.query, self.dbnotes)
        self.bsid.first()
        self.ui.spinBsid.setValue(self.bsid.value('bsmax'))
        self.bsid.finish()
        ##### first QSQlquery above
        self.query = "select max(bpid) as bpmax from vsigns_bp"
        self.bpid = QSqlQuery(self.query, self.dbnotes)
        self.bpid.first()
        self.ui.spinBpid.setValue(self.bpid.value('bpmax'))
        self.bpid.finish()
        #### second above

        ### get last note from table
        self.query = f"select fnotes, foodid from {self.table_name} where foodid = (select max(foodid) from {self.table_name})"
        self.fnotes = QSqlQuery(self.query, self.dbnotes)
        self.fnotes.first()
        self.ui.textEdit.setText(self.fnotes.value('fnotes'))
        self.foodid = self.fnotes.value('foodid')
        self.fnotes.finish()
        # table
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("vsigns_bp")
        self.model.setFilter("bpid = (select max(bpid) from vsigns_bp)")
        self.model.select()
        self.tbl = self.ui.tblPrevRec
        self.tbl.setModel(self.model)
        debug(QSqlDatabase.connectionNames())

    def update_rec(self):
        self.query = f"""
            update {self.table_name} SET
            fdate = '{self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm")}',
            fnotes = '{self.ui.textEdit.toPlainText()}',
            sugarid = {self.ui.spinBsid.value()},
            bpid = {self.ui.spinBpid.value()}
            where foodid = {self.foodid}
            """

        self.updatedata = QSqlQuery(self.query, self.dbnotes)
        self.upok = self.updatedata.exec()
     # debug for update problem
        #debug(self.upok)
        #debug(self.query)
        if self.upok :
            self.ui.lblRecord2.setText(f"update rec {self.table_name}")
        else:
            self.ui.lblRecord2.setText(f"no update  {self.table_name}")

        self.populate_boxes()

    def add_rec(self):
        self.insertdata = QSqlQuery(self.dbnotes)
        self.insertdata.prepare(
            f"""
            insert into {self.table_name}( 
            fdate,
            fnotes,
            sugarid,
            bpid
            )
            VALUES (?,?,?,?)
            """ )
        self.insertdata.addBindValue(self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm"))
        self.insertdata.addBindValue(self.ui.textEdit.toPlainText())
        self.insertdata.addBindValue(self.ui.spinBsid.value())
        self.insertdata.addBindValue(self.ui.spinBpid.value())
        self.insertok = self.insertdata.exec()
        if self.insertok :
            self.ui.lblRecord2.setText(f"rec add {self.table_name}")
        else:
            self.ui.lblRecord2.setText(f"NO REC {self.table_name}")
        self.populate_boxes()



    def closeDatabase(self):
        self.tbl.setModel(None)
        del self.model
        self.dbnotes.close()
        del self.dbnotes
        self.db.close()
        del self.db
        # rfile edit April fool
        QSqlDatabase.removeDatabase(self.conn_rec)
        QSqlDatabase.removeDatabase(self.conn_name)
        debug(QSqlDatabase.connectionNames())

    def exitfunc(self):
        print('exitfunc triggered')
        self.closeDatabase()
        self.close()

    def closeEvent(self, event):
        print('close event func triggered')
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
