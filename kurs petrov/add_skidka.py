# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_skidka.ui'
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
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(350, 222)
        Form.setStyleSheet("background-color: rgb(245, 194, 17);")
        self.number_lbl1 = QtWidgets.QLabel(Form)
        self.number_lbl1.setGeometry(QtCore.QRect(10, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.number_lbl1.setFont(font)
        self.number_lbl1.setObjectName("number_lbl1")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 40, 113, 26))
        self.lineEdit.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.lineEdit.setObjectName("lineEdit")
        self.skidki_lbl = QtWidgets.QLabel(Form)
        self.skidki_lbl.setGeometry(QtCore.QRect(10, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.skidki_lbl.setFont(font)
        self.skidki_lbl.setObjectName("skidki_lbl")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(170, 90, 111, 31))
        self.spinBox.setObjectName("spinBox")
        self.add_btn = QtWidgets.QPushButton(Form)
        self.add_btn.setGeometry(QtCore.QRect(80, 160, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить скидку"))
        self.number_lbl1.setText(_translate("Form", "номер товара"))
        self.lineEdit.setText(_translate("Form", "0"))
        self.skidki_lbl.setText(_translate("Form", "размер скидки"))
        self.add_btn.setText(_translate("Form", "добавить"))