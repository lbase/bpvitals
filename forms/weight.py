# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weight.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Weight(object):
    def setupUi(self, Weight):
        Weight.setObjectName("Weight")
        Weight.resize(640, 598)
        self.btnSubmit = QtWidgets.QPushButton(Weight)
        self.btnSubmit.setGeometry(QtCore.QRect(420, 40, 131, 31))
        self.btnSubmit.setObjectName("btnSubmit")
        self.txtMsgbox = QtWidgets.QPlainTextEdit(Weight)
        self.txtMsgbox.setGeometry(QtCore.QRect(30, 520, 541, 51))
        self.txtMsgbox.setObjectName("txtMsgbox")
        self.btnWeightchart = QtWidgets.QPushButton(Weight)
        self.btnWeightchart.setGeometry(QtCore.QRect(430, 110, 102, 31))
        self.btnWeightchart.setObjectName("btnWeightchart")
        self.layoutWidget = QtWidgets.QWidget(Weight)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 328, 471))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblTime = QtWidgets.QLabel(self.layoutWidget)
        self.lblTime.setObjectName("lblTime")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblTime)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateTimeEdit)
        self.lblWeight = QtWidgets.QLabel(self.layoutWidget)
        self.lblWeight.setObjectName("lblWeight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblWeight)
        self.spnWeight = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spnWeight.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnWeight.setMinimum(200.0)
        self.spnWeight.setMaximum(310.0)
        self.spnWeight.setObjectName("spnWeight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spnWeight)
        self.lblBmi = QtWidgets.QLabel(self.layoutWidget)
        self.lblBmi.setObjectName("lblBmi")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblBmi)
        self.spnBmi = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spnBmi.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnBmi.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spnBmi.setMinimum(20.0)
        self.spnBmi.setMaximum(40.0)
        self.spnBmi.setSingleStep(0.1)
        self.spnBmi.setObjectName("spnBmi")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spnBmi)
        self.lblBodyfat = QtWidgets.QLabel(self.layoutWidget)
        self.lblBodyfat.setObjectName("lblBodyfat")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblBodyfat)
        self.spnBodyfat = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spnBodyfat.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnBodyfat.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spnBodyfat.setMinimum(20.0)
        self.spnBodyfat.setMaximum(50.0)
        self.spnBodyfat.setSingleStep(1.0)
        self.spnBodyfat.setObjectName("spnBodyfat")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spnBodyfat)
        self.lblFatfree = QtWidgets.QLabel(self.layoutWidget)
        self.lblFatfree.setObjectName("lblFatfree")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblFatfree)
        self.spnFatfree = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spnFatfree.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnFatfree.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spnFatfree.setMinimum(120.0)
        self.spnFatfree.setMaximum(180.0)
        self.spnFatfree.setSingleStep(1.0)
        self.spnFatfree.setProperty("value", 120.0)
        self.spnFatfree.setObjectName("spnFatfree")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spnFatfree)
        self.lblSubfat = QtWidgets.QLabel(self.layoutWidget)
        self.lblSubfat.setObjectName("lblSubfat")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblSubfat)
        self.spnSubfat = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spnSubfat.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnSubfat.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spnSubfat.setMinimum(20.0)
        self.spnSubfat.setMaximum(40.0)
        self.spnSubfat.setSingleStep(1.0)
        self.spnSubfat.setObjectName("spnSubfat")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spnSubfat)
        self.lblViscfat = QtWidgets.QLabel(self.layoutWidget)
        self.lblViscfat.setObjectName("lblViscfat")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lblViscfat)
        self.spnViscfat = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spnViscfat.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnViscfat.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spnViscfat.setMinimum(10.0)
        self.spnViscfat.setMaximum(30.0)
        self.spnViscfat.setSingleStep(1.0)
        self.spnViscfat.setProperty("value", 10.0)
        self.spnViscfat.setObjectName("spnViscfat")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spnViscfat)
        self.lblWater = QtWidgets.QLabel(self.layoutWidget)
        self.lblWater.setObjectName("lblWater")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lblWater)
        self.spnWater = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spnWater.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnWater.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spnWater.setMinimum(35.0)
        self.spnWater.setMaximum(50.0)
        self.spnWater.setSingleStep(1.0)
        self.spnWater.setObjectName("spnWater")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.spnWater)
        self.lblSkelmuscle = QtWidgets.QLabel(self.layoutWidget)
        self.lblSkelmuscle.setObjectName("lblSkelmuscle")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.lblSkelmuscle)
        self.spnSkelmuscle = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spnSkelmuscle.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnSkelmuscle.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spnSkelmuscle.setMinimum(30.0)
        self.spnSkelmuscle.setMaximum(50.0)
        self.spnSkelmuscle.setSingleStep(0.1)
        self.spnSkelmuscle.setProperty("value", 30.0)
        self.spnSkelmuscle.setObjectName("spnSkelmuscle")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.spnSkelmuscle)
        self.lblMuscle = QtWidgets.QLabel(self.layoutWidget)
        self.lblMuscle.setObjectName("lblMuscle")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.lblMuscle)
        self.spnMuscle = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spnMuscle.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnMuscle.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spnMuscle.setMinimum(140.0)
        self.spnMuscle.setMaximum(200.0)
        self.spnMuscle.setSingleStep(1.0)
        self.spnMuscle.setObjectName("spnMuscle")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.spnMuscle)
        self.lblBonemass = QtWidgets.QLabel(self.layoutWidget)
        self.lblBonemass.setObjectName("lblBonemass")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.lblBonemass)
        self.spnBonemass = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spnBonemass.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnBonemass.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spnBonemass.setMinimum(6.0)
        self.spnBonemass.setMaximum(9.0)
        self.spnBonemass.setSingleStep(0.1)
        self.spnBonemass.setProperty("value", 6.0)
        self.spnBonemass.setObjectName("spnBonemass")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.spnBonemass)
        self.lblProtein = QtWidgets.QLabel(self.layoutWidget)
        self.lblProtein.setObjectName("lblProtein")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.lblProtein)
        self.spnProtein = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spnProtein.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnProtein.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spnProtein.setMinimum(10.0)
        self.spnProtein.setMaximum(20.0)
        self.spnProtein.setSingleStep(1.0)
        self.spnProtein.setProperty("value", 10.0)
        self.spnProtein.setObjectName("spnProtein")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.spnProtein)
        self.lblBmr = QtWidgets.QLabel(self.layoutWidget)
        self.lblBmr.setObjectName("lblBmr")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.lblBmr)
        self.spnBmr = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spnBmr.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnBmr.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spnBmr.setMinimum(1800.0)
        self.spnBmr.setMaximum(2000.0)
        self.spnBmr.setSingleStep(10.0)
        self.spnBmr.setObjectName("spnBmr")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.spnBmr)
        self.lblAge = QtWidgets.QLabel(self.layoutWidget)
        self.lblAge.setObjectName("lblAge")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.lblAge)
        self.spnAge = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spnAge.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnAge.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spnAge.setMinimum(70.0)
        self.spnAge.setMaximum(80.0)
        self.spnAge.setSingleStep(1.0)
        self.spnAge.setObjectName("spnAge")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.spnAge)
        self.btnExit = QtWidgets.QPushButton(Weight)
        self.btnExit.setGeometry(QtCore.QRect(430, 180, 71, 31))
        self.btnExit.setObjectName("btnExit")
        self.lblTime.setBuddy(self.dateTimeEdit)
        self.lblWeight.setBuddy(self.spnWeight)
        self.lblBmi.setBuddy(self.spnBmi)
        self.lblBodyfat.setBuddy(self.spnBodyfat)
        self.lblFatfree.setBuddy(self.spnFatfree)
        self.lblSubfat.setBuddy(self.spnSubfat)
        self.lblViscfat.setBuddy(self.spnViscfat)
        self.lblWater.setBuddy(self.spnWater)
        self.lblSkelmuscle.setBuddy(self.spnSkelmuscle)
        self.lblMuscle.setBuddy(self.spnMuscle)
        self.lblBonemass.setBuddy(self.spnBonemass)
        self.lblProtein.setBuddy(self.spnProtein)
        self.lblBmr.setBuddy(self.spnBmr)
        self.lblAge.setBuddy(self.spnAge)

        self.retranslateUi(Weight)
        QtCore.QMetaObject.connectSlotsByName(Weight)
        Weight.setTabOrder(self.dateTimeEdit, self.spnWeight)
        Weight.setTabOrder(self.spnWeight, self.spnBmi)
        Weight.setTabOrder(self.spnBmi, self.spnBodyfat)
        Weight.setTabOrder(self.spnBodyfat, self.spnFatfree)
        Weight.setTabOrder(self.spnFatfree, self.spnSubfat)
        Weight.setTabOrder(self.spnSubfat, self.spnViscfat)
        Weight.setTabOrder(self.spnViscfat, self.spnWater)
        Weight.setTabOrder(self.spnWater, self.spnSkelmuscle)
        Weight.setTabOrder(self.spnSkelmuscle, self.spnMuscle)
        Weight.setTabOrder(self.spnMuscle, self.spnBonemass)
        Weight.setTabOrder(self.spnBonemass, self.spnProtein)
        Weight.setTabOrder(self.spnProtein, self.spnBmr)
        Weight.setTabOrder(self.spnBmr, self.spnAge)
        Weight.setTabOrder(self.spnAge, self.btnSubmit)
        Weight.setTabOrder(self.btnSubmit, self.txtMsgbox)
        Weight.setTabOrder(self.txtMsgbox, self.btnWeightchart)

    def retranslateUi(self, Weight):
        _translate = QtCore.QCoreApplication.translate
        Weight.setWindowTitle(_translate("Weight", "Dialog"))
        self.btnSubmit.setText(_translate("Weight", "Add &Rec"))
        self.btnWeightchart.setText(_translate("Weight", "Wt Chart"))
        self.lblTime.setText(_translate("Weight", "Date"))
        self.lblWeight.setText(_translate("Weight", "Weight"))
        self.spnWeight.setToolTip(_translate("Weight", "weight in pounds"))
        self.lblBmi.setText(_translate("Weight", "BMI"))
        self.lblBodyfat.setText(_translate("Weight", "BodyFat"))
        self.lblFatfree.setText(_translate("Weight", "FatFreeWt"))
        self.lblSubfat.setText(_translate("Weight", "SubC Fat"))
        self.lblViscfat.setText(_translate("Weight", "Visc Fat"))
        self.lblWater.setText(_translate("Weight", "Body Water"))
        self.lblSkelmuscle.setText(_translate("Weight", "Skeletal Muscle"))
        self.lblMuscle.setText(_translate("Weight", "Muscle Mass"))
        self.lblBonemass.setText(_translate("Weight", "Bone Mass"))
        self.lblProtein.setText(_translate("Weight", "Protein"))
        self.lblBmr.setText(_translate("Weight", "BMR"))
        self.lblAge.setText(_translate("Weight", "Metabolic Age"))
        self.btnExit.setText(_translate("Weight", "Exit"))
