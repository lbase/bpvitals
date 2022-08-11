#! /usr/bin/env python3

import sys
import os
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiSubWindow,  QAction
from PyQt5.QtCore import QCoreApplication
from icecream import ic
from devtools import debug
from forms.mdiview import Ui_MainWindow
from sugar_code import Main as Msugar
from graphs import modbpstats
from vitals_code import Main as VMain
from showquery import MainWindow as qryWin

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #============================================================
    #             menu setup
    #==========================================================
        self.ui.actionRec_Vitals.triggered.connect(self.add_Vmain)
        self.ui.actionView.triggered.connect(self.add_showquery)
        self.ui.actionRec_sugar.triggered.connect(self.recsugar)
        

    def add_Vmain(self):
        self.vsub = QMdiSubWindow()
        #self.vm = VMain()
        self.vsub.setWidget(VMain())
        self.add_vmain = self.ui.mdiArea.addSubWindow(self.vsub)
        self.add_vmain.resize(QSize(600,400))
        self.add_vmain.show()
    def add_showquery(self):
        self.ssub = QMdiSubWindow()
        self.ssub.setWidget(qryWin())
        self.add_show = self.ui.mdiArea.addSubWindow(self.ssub)
        self.add_show.resize(QSize(600,600))
        self.add_show.show()

    def recsugar(self):
        self.sugarsub = QMdiSubWindow()
        self.sugarsub.setWidget(Msugar(self))
        self.addsugar = self.ui.mdiArea.addSubWindow(self.sugarsub)
        self.addsugar.resize(QSize(800,600))
        self.addsugar.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()        



        
