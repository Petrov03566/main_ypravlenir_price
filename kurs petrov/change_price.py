# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_price.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QMainWindow): 
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 230)
        Form.setStyleSheet("background-color: rgb(245, 194, 17);")
        self.number_lineEdit = QtWidgets.QLineEdit(Form)
        self.number_lineEdit.setGeometry(QtCore.QRect(200, 40, 113, 26))
        self.number_lineEdit.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.number_lineEdit.setObjectName("number_lineEdit")
        self.change = QtWidgets.QPushButton(Form)
        self.change.setGeometry(QtCore.QRect(70, 150, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.change.setFont(font)
        self.change.setObjectName("change")
        self.number_lbl1 = QtWidgets.QLabel(Form)
        self.number_lbl1.setGeometry(QtCore.QRect(40, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.number_lbl1.setFont(font)
        self.number_lbl1.setObjectName("number_lbl1")
        self.price_lbl = QtWidgets.QLabel(Form)
        self.price_lbl.setGeometry(QtCore.QRect(40, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.price_lbl.setFont(font)
        self.price_lbl.setObjectName("price_lbl")
        self.number_lineEdit2 = QtWidgets.QLineEdit(Form)
        self.number_lineEdit2.setGeometry(QtCore.QRect(200, 90, 113, 26))
        self.number_lineEdit2.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.number_lineEdit2.setObjectName("number_lineEdit2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Изменить цену "))
        self.number_lineEdit.setText(_translate("Form", "0"))
        self.change.setText(_translate("Form", "изменить"))
        self.number_lbl1.setText(_translate("Form", "номер товара"))
        self.price_lbl.setText(_translate("Form", " цена"))
        self.number_lineEdit2.setText(_translate("Form", "0"))