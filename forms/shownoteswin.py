# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shownoteswin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NotesWin(object):
    def setupUi(self, NotesWin):
        NotesWin.setObjectName("NotesWin")
        NotesWin.resize(898, 646)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(NotesWin.sizePolicy().hasHeightForWidth())
        NotesWin.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(NotesWin)
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
        sizePolicy.setVerticalStretch(24)
        sizePolicy.setHeightForWidth(self.tb1.sizePolicy().hasHeightForWidth())
        self.tb1.setSizePolicy(sizePolicy)
        self.tb1.setMinimumSize(QtCore.QSize(100, 0))
        self.tb1.setLineWidth(2)
        self.tb1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tb1.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tb1.setObjectName("tb1")
        self.gridLayout.addWidget(self.tb1, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btnGraphbp = QtWidgets.QPushButton(self.splitter)
        self.btnGraphbp.setObjectName("btnGraphbp")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        NotesWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NotesWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 34))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        NotesWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NotesWin)
        self.statusbar.setObjectName("statusbar")
        NotesWin.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(NotesWin)
        self.toolBar.setObjectName("toolBar")
        NotesWin.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtWidgets.QAction(NotesWin)
        self.actionExit.setObjectName("actionExit")
        self.menu_File.addAction(self.actionExit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(NotesWin)
        QtCore.QMetaObject.connectSlotsByName(NotesWin)

    def retranslateUi(self, NotesWin):
        _translate = QtCore.QCoreApplication.translate
        NotesWin.setWindowTitle(_translate("NotesWin", "MainWindow"))
        self.btnGraphbp.setText(_translate("NotesWin", "Graph BP"))
        self.menu_File.setTitle(_translate("NotesWin", "&File"))
        self.toolBar.setWindowTitle(_translate("NotesWin", "toolBar"))
        self.actionExit.setText(_translate("NotesWin", "Exit"))
