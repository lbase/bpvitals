
import datetime

from icecream.icecream import IceCreamDebugger
from notes import Ui_Comment
from notes import Ui_Comment
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, QModelIndex, QSize, QSizeF
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QDataWidgetMapper, QTableView
import sqlalchemy as dbsql
from sqlalchemy.orm import sessionmaker
from icecream import ic
import sys
class Main(QtWidgets.QWidget, Ui_Comment):
    """docstring for Main
"""
    def __init__(self, table_name="mynotes"):
        super(Main, self).__init__()
        self.table_name = table_name
        self.ui = Ui_Comment()
        self.ui.setupUi(self)

        # self.conn_notes = self.eng.connect()  # use this as connection for insert query
         # ---------------------------------------------------------------------------- #
         #           make sqlalchemy session and database connection                    #
         # ---------------------------------------------------------------------------- #
        self.eng = dbsql.create_engine(
            "sqlite:////home/rfile/python3/bpvitals/vitals.db")
        self.mysession = sessionmaker(bind=self.eng)
        self.mysess = self.mysession()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("/home/rfile/python3/bpvitals/vitals.db")
        self.ok = self.db.open()
        ic(self.ok , self.db.driverName())

         # ---------------------------------------------------------------------------- #
         #              table name in window title so I can tell what table              #
         # ---------------------------------------------------------------------------- #
        self.setWindowTitle(table_name)
        # current date
        now = QDateTime.currentDateTime()
        self.ui.dateTimeEdit.setDateTime(now)
        # buttons
        self.ui.btnAdd.clicked.connect(self.add_rec)
        self.ui.btnUpdate.clicked.connect(self.update_rec)
        self.populate_boxes()
        # ---------------------------------------------------------------------------- #
        #                      get numbers and one previous record                     #
        # ---------------------------------------------------------------------------- #

    def populate_boxes(self):
        self.bsid = self.mysess.execute("select max(bsid) as 'bsmax' from qtsugar")
        self.spin_s = self.bsid.fetchone()
        self.ui.spinBsid.setValue(self.spin_s.bsmax)
        self.bpid = self.mysess.execute("select max(bpid) as 'bpmax' from vsigns_bp")
        self.spin_bp = self.bpid.fetchone()
        self.ui.spinBpid.setValue(self.spin_bp.bpmax)
        self.texbx = self.mysess.execute("select fnotes from mynotes where foodid = (select max(foodid) from mynotes)")
        self.texbx_txt = self.texbx.fetchone()
        self.ui.textEdit.setText(self.texbx_txt.fnotes)

        self.model = QSqlTableModel(db=self.db)
        self.model.setTable("vsigns_bp")
        self.model.setFilter('bpid = (select max(bpid) from vsigns_bp)')
        self.model.select()

        self.tbl = self.ui.tblPrevRec
        self.tbl.setModel(self.model)


        ic(self.ok)
        ic(self.model.filter())
        ic(self.model.lastError().type())
        ic(self.model.lastError().text())
        ic(self.model.tableName())
        ic(self.model.select())
        # ic(self.db.connectionNames())
        # ic(self.db.tables())



    def update_rec(self):
        self.note = self.ui.textEdit.toPlainText()
        self.id = str(self.ui.spinBpid.value())
        self.stmt = "update mynotes set fnotes  = " + " '" + self.note + "' " + "where bpid = 681"
        ic(self.stmt)
        self.mysess.execute(self.stmt)
        self.mysess.commit()

    def add_rec(self):
        self.my_table = dbsql.table(self.table_name, dbsql.column("fdate"),\
            dbsql.column("sugarid"), dbsql.column("bpid"),\
            dbsql.column("fnotes"))
        self.ins = self.my_table.insert().values({"fdate": self.ui.dateTimeEdit.dateTime().toString(),\
            "fnotes": self.ui.textEdit.toPlainText(),\
                "sugarid": self.ui.spinBsid.value(), "bpid": self.ui.spinBpid.value()})
        self.result = self.mysess.execute(self.ins)
        self.mysess.commit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())