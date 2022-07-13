import sys
import os
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiSubWindow, QTableView, QWidget, QAction
from PyQt5.QtCore import QCoreApplication
from icecream import ic
from mdiview import Ui_MainWindow
from vitals_code import Main as VMain
from showquery import MainWindow as qryWin

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.actionAdd_New.triggered.connect(self.add_Vmain)
        self.ui.actionAdd_New.triggered.connect(self.add_Vmain)
        self.ui.actionView.triggered.connect(self.add_showquery)
        

    def add_Vmain(self):
        self.vsub = QMdiSubWindow()
        #self.vm = VMain()
        self.vsub.setWidget(VMain())
        self.add_vmain = self.ui.mdiArea.addSubWindow(self.vsub)
        self.add_vmain.resize(QSize(400,400))
        self.add_vmain.show()
    def add_showquery(self):
        self.ssub = QMdiSubWindow()
        self.ssub.setWidget(qryWin())
        self.add_show = self.ui.mdiArea.addSubWindow(self.ssub)
        self.add_show.resize(QSize(600,600))
        self.add_show.show()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()        



        
