# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './showquerywin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 646)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tb1 = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb1.sizePolicy().hasHeightForWidth())
        self.tb1.setSizePolicy(sizePolicy)
        self.tb1.setMinimumSize(QtCore.QSize(100, 0))
        self.tb1.setLineWidth(2)
        self.tb1.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tb1.setObjectName("tb1")
        self.tb1.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tb1, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btnRefresh = QtWidgets.QPushButton(self.splitter)
        self.btnRefresh.setObjectName("btnRefresh")
        self.btnVform = QtWidgets.QPushButton(self.splitter)
        self.btnVform.setObjectName("btnVform")
        self.btnDelete = QtWidgets.QPushButton(self.splitter)
        self.btnDelete.setObjectName("btnDelete")
        self.btnGraphbp = QtWidgets.QPushButton(self.splitter)
        self.btnGraphbp.setObjectName("btnGraphbp")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 31))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu_File.addAction(self.actionExit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnRefresh.setText(_translate("MainWindow", "Refresh"))
        self.btnVform.setText(_translate("MainWindow", "Add &New"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnGraphbp.setText(_translate("MainWindow", "Graph BP"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))