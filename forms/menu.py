# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(1247, 692)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Menu.sizePolicy().hasHeightForWidth())
        Menu.setSizePolicy(sizePolicy)
        Menu.setMaximumSize(QtCore.QSize(1247, 692))
        self.lblComment = QtWidgets.QLabel(Menu)
        self.lblComment.setGeometry(QtCore.QRect(10, 8, 209, 21))
        self.lblComment.setObjectName("lblComment")
        self.txtComment = QtWidgets.QPlainTextEdit(Menu)
        self.txtComment.setGeometry(QtCore.QRect(10, 40, 621, 51))
        self.txtComment.setPlainText("")
        self.txtComment.setObjectName("txtComment")
        self.chkPG = QtWidgets.QCheckBox(Menu)
        self.chkPG.setGeometry(QtCore.QRect(510, 10, 94, 26))
        self.chkPG.setObjectName("chkPG")
        self.btnInsert = QtWidgets.QPushButton(Menu)
        self.btnInsert.setGeometry(QtCore.QRect(110, 100, 75, 31))
        self.btnInsert.setObjectName("btnInsert")
        self.sugarCombo = QtWidgets.QComboBox(Menu)
        self.sugarCombo.setGeometry(QtCore.QRect(200, 100, 93, 27))
        self.sugarCombo.setEditable(True)
        self.sugarCombo.setObjectName("sugarCombo")
        self.lblInsert = QtWidgets.QLabel(Menu)
        self.lblInsert.setGeometry(QtCore.QRect(310, 10, 121, 21))
        self.lblInsert.setObjectName("lblInsert")
        self.btnExit = QtWidgets.QPushButton(Menu)
        self.btnExit.setGeometry(QtCore.QRect(20, 100, 75, 31))
        self.btnExit.setObjectName("btnExit")
        self.lblSugar = QtWidgets.QLabel(Menu)
        self.lblSugar.setGeometry(QtCore.QRect(220, 130, 49, 21))
        self.lblSugar.setObjectName("lblSugar")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Menu)
        self.dateTimeEdit.setGeometry(QtCore.QRect(310, 100, 211, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.btnGraph48 = QtWidgets.QPushButton(Menu)
        self.btnGraph48.setGeometry(QtCore.QRect(640, 40, 151, 31))
        self.btnGraph48.setObjectName("btnGraph48")
        self.btnGraph8 = QtWidgets.QPushButton(Menu)
        self.btnGraph8.setGeometry(QtCore.QRect(640, 80, 151, 31))
        self.btnGraph8.setObjectName("btnGraph8")
        self.btnVitals = QtWidgets.QPushButton(Menu)
        self.btnVitals.setGeometry(QtCore.QRect(800, 40, 102, 31))
        self.btnVitals.setObjectName("btnVitals")
        self.tblViewRec = QtWidgets.QTableView(Menu)
        self.tblViewRec.setGeometry(QtCore.QRect(10, 320, 1221, 361))
        self.tblViewRec.setObjectName("tblViewRec")
        self.tblViewRec.horizontalHeader().setStretchLastSection(True)
        self.btnShowBP = QtWidgets.QPushButton(Menu)
        self.btnShowBP.setGeometry(QtCore.QRect(800, 80, 102, 31))
        self.btnShowBP.setObjectName("btnShowBP")
        self.txtMsgs = QtWidgets.QPlainTextEdit(Menu)
        self.txtMsgs.setGeometry(QtCore.QRect(10, 253, 1221, 61))
        self.txtMsgs.setObjectName("txtMsgs")
        self.btnRefresh = QtWidgets.QPushButton(Menu)
        self.btnRefresh.setGeometry(QtCore.QRect(530, 100, 102, 31))
        self.btnRefresh.setObjectName("btnRefresh")
        self.btnWeight = QtWidgets.QPushButton(Menu)
        self.btnWeight.setGeometry(QtCore.QRect(910, 40, 151, 31))
        self.btnWeight.setObjectName("btnWeight")
        self.btnWeightshow = QtWidgets.QPushButton(Menu)
        self.btnWeightshow.setGeometry(QtCore.QRect(910, 80, 151, 31))
        self.btnWeightshow.setObjectName("btnWeightshow")
        self.btnFoodnotes = QtWidgets.QPushButton(Menu)
        self.btnFoodnotes.setGeometry(QtCore.QRect(1070, 40, 102, 31))
        self.btnFoodnotes.setObjectName("btnFoodnotes")
        self.btnFastnotes = QtWidgets.QPushButton(Menu)
        self.btnFastnotes.setGeometry(QtCore.QRect(1070, 80, 102, 31))
        self.btnFastnotes.setObjectName("btnFastnotes")

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.lblComment.setText(_translate("Menu", "Comment for new record:"))
        self.chkPG.setText(_translate("Menu", "Postgres"))
        self.btnInsert.setText(_translate("Menu", "A&dd"))
        self.lblInsert.setText(_translate("Menu", "Insert Rec"))
        self.btnExit.setText(_translate("Menu", "E&xit"))
        self.lblSugar.setText(_translate("Menu", "Sugar"))
        self.btnGraph48.setText(_translate("Menu", "&Graph 48 hrs"))
        self.btnGraph8.setText(_translate("Menu", "&Graph 8 days"))
        self.btnVitals.setText(_translate("Menu", "Vitals"))
        self.btnShowBP.setText(_translate("Menu", "Show BP"))
        self.btnRefresh.setText(_translate("Menu", "refresh"))
        self.btnWeight.setText(_translate("Menu", "Weight Chart"))
        self.btnWeightshow.setText(_translate("Menu", "Weight Entry"))
        self.btnFoodnotes.setText(_translate("Menu", "Food Notes"))
        self.btnFastnotes.setText(_translate("Menu", "Fast Notes"))
