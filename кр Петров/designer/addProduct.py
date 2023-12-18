# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addProduct.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class AppProduct(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(293, 404)
        Form.setStyleSheet("background-color: rgb(229, 165, 10);")
        self.add_product_btn = QtWidgets.QPushButton(Form)
        self.add_product_btn.setGeometry(QtCore.QRect(20, 330, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.add_product_btn.setFont(font)
        self.add_product_btn.setObjectName("add_product_btn")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 70, 221, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"border-radius: 20px;\n"
"border: rgb(255, 163, 72);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 30, 91, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 170, 221, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"border-radius: 20px;\n"
"border: rgb(255, 163, 72);\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 260, 221, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"border-radius: 20px;\n"
"border: rgb(255, 163, 72);\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 230, 121, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить товар"))
        self.add_product_btn.setText(_translate("Form", "добавить товар"))
        self.label.setText(_translate("Form", "Название"))
        self.label_2.setText(_translate("Form", "Стоимость (в рублях)"))
        self.label_3.setText(_translate("Form", "Количество"))
