# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addManeger.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(412, 594)
        Form.setStyleSheet("background-color: rgb(229, 165, 10);")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 250, 221, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"border-radius: 20px;\n"
"border: rgb(255, 163, 72);\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 30, 91, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 221, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"border-radius: 20px;\n"
"border: rgb(255, 163, 72);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 160, 221, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"border-radius: 20px;\n"
"border: rgb(255, 163, 72);\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 220, 121, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 340, 221, 41))
        self.lineEdit_4.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"border-radius: 20px;\n"
"border: rgb(255, 163, 72);\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(150, 310, 121, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 430, 221, 41))
        self.lineEdit_5.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"border-radius: 20px;\n"
"border: rgb(255, 163, 72);\n"
"")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(150, 400, 121, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.add_product_btn_2 = QtWidgets.QPushButton(Form)
        self.add_product_btn_2.setGeometry(QtCore.QRect(80, 510, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.add_product_btn_2.setFont(font)
        self.add_product_btn_2.setObjectName("add_product_btn_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "добавить менеджера"))
        self.label_2.setText(_translate("Form", "Фамилия"))
        self.label.setText(_translate("Form", "Имя"))
        self.label_3.setText(_translate("Form", "Отчество"))
        self.label_4.setText(_translate("Form", "Логин"))
        self.label_5.setText(_translate("Form", "Пароль"))
        self.add_product_btn_2.setText(_translate("Form", "Добавить менеджера"))
