# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mdiview.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 623)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRecord = QtWidgets.QMenu(self.menubar)
        self.menuRecord.setObjectName("menuRecord")
        self.menuGraphs = QtWidgets.QMenu(self.menubar)
        self.menuGraphs.setObjectName("menuGraphs")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRec_Vitals = QtWidgets.QAction(MainWindow)
        self.actionRec_Vitals.setObjectName("actionRec_Vitals")
        self.actionView = QtWidgets.QAction(MainWindow)
        self.actionView.setObjectName("actionView")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionRec_sugar = QtWidgets.QAction(MainWindow)
        self.actionRec_sugar.setObjectName("actionRec_sugar")
        self.actionSugar_8_days = QtWidgets.QAction(MainWindow)
        self.actionSugar_8_days.setObjectName("actionSugar_8_days")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuRecord.addAction(self.actionRec_Vitals)
        self.menuRecord.addAction(self.actionView)
        self.menuRecord.addAction(self.actionRec_sugar)
        self.menuGraphs.addAction(self.actionSugar_8_days)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRecord.menuAction())
        self.menubar.addAction(self.menuGraphs.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuRecord.setTitle(_translate("MainWindow", "Record"))
        self.menuGraphs.setTitle(_translate("MainWindow", "Graphs"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionRec_Vitals.setText(_translate("MainWindow", "rec Vitals"))
        self.actionView.setText(_translate("MainWindow", "View BP records"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRec_sugar.setText(_translate("MainWindow", "rec sugar"))
        self.actionSugar_8_days.setText(_translate("MainWindow", "Sugar 8 days"))