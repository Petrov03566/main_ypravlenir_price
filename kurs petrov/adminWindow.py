# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adn2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin_window(QtWidgets.QMainWindow):
    def setupUi(self, Admin_window):
        Admin_window.setObjectName("Admin_window")
        Admin_window.resize(534, 681)
        Admin_window.setStyleSheet("background-color: rgb(229, 165, 10);")
        self.label_tov = QtWidgets.QLabel(Admin_window)
        self.label_tov.setGeometry(QtCore.QRect(160, 10, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_tov.setFont(font)
        self.label_tov.setStyleSheet("")
        self.label_tov.setObjectName("label_tov")
        self.push_db = QtWidgets.QPushButton(Admin_window)
        self.push_db.setGeometry(QtCore.QRect(10, 610, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_db.setFont(font)
        self.push_db.setObjectName("push_db")
        
        self.label_3 = QtWidgets.QLabel(Admin_window)
        self.label_3.setGeometry(QtCore.QRect(20, 440, 241, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Admin_window)
        self.label.setGeometry(QtCore.QRect(20, 350, 281, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(46, 194, 126);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Admin_window)
        self.label_2.setGeometry(QtCore.QRect(20, 350, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Admin_window)
        self.lineEdit.setGeometry(QtCore.QRect(10, 380, 501, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"border-radius: 20px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Admin_window)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 460, 501, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"border-radius: 20px;\n"
"\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(Admin_window)
        self.label_6.setGeometry(QtCore.QRect(20, 520, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(Admin_window)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 550, 501, 41))
        self.lineEdit_4.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"border-radius: 20px;\n"
"\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.tableView = QtWidgets.QTableView(Admin_window)
        self.tableView.setGeometry(QtCore.QRect(10, 50, 511, 301))
        self.tableView.setStyleSheet("background-color: rgb(233, 241, 250);")
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Admin_window)
        QtCore.QMetaObject.connectSlotsByName(Admin_window)

    def retranslateUi(self, Admin_window):
        _translate = QtCore.QCoreApplication.translate
        Admin_window.setWindowTitle(_translate("Admin_window", "adn"))
        self.label_tov.setText(_translate("Admin_window", "Список товаров"))
        self.push_db.setText(_translate("Admin_window", "добавить товары"))
        self.label_3.setText(_translate("Admin_window", "Товар"))
        self.label_2.setText(_translate("Admin_window", "Срок годности"))
        self.label_6.setText(_translate("Admin_window", "Цена на товара"))
