# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindowAdmin(QtWidgets.QWidget):
    def setupUi(self, Admin_window):
        Admin_window.setObjectName("Admin_window")
        Admin_window.resize(1051, 501)
        Admin_window.setStyleSheet("background-color: rgb(229, 165, 10);")
        self.title_lbl = QtWidgets.QLabel(Admin_window)
        self.title_lbl.setGeometry(QtCore.QRect(160, 0, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title_lbl.setFont(font)
        self.title_lbl.setStyleSheet("")
        self.title_lbl.setObjectName("title_lbl")
        self.add_product_btn = QtWidgets.QPushButton(Admin_window)
        self.add_product_btn.setGeometry(QtCore.QRect(40, 410, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.add_product_btn.setFont(font)
        self.add_product_btn.setObjectName("add_product_btn")
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
        self.tableView_product = QtWidgets.QTableView(Admin_window)
        self.tableView_product.setGeometry(QtCore.QRect(10, 50, 511, 301))
        self.tableView_product.setStyleSheet("background-color: rgb(233, 241, 250);")
        self.tableView_product.setObjectName("tableView")
        self.create_report_btn = QtWidgets.QPushButton(Admin_window)
        self.create_report_btn.setGeometry(QtCore.QRect(770, 410, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.create_report_btn.setFont(font)
        self.create_report_btn.setObjectName("create_report_btn")
        self.add_maneger_btn = QtWidgets.QPushButton(Admin_window)
        self.add_maneger_btn.setGeometry(QtCore.QRect(410, 410, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.add_maneger_btn.setFont(font)
        self.add_maneger_btn.setObjectName("add_maneger_btn")
        self.tableView_user = QtWidgets.QTableView(Admin_window)
        self.tableView_user.setGeometry(QtCore.QRect(550, 50, 491, 301))
        self.tableView_user.setStyleSheet("background-color: rgb(233, 241, 250);")
        self.tableView_user.setObjectName("tableView_2")
        self.title_lbl_2 = QtWidgets.QLabel(Admin_window)
        self.title_lbl_2.setGeometry(QtCore.QRect(700, 0, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title_lbl_2.setFont(font)
        self.title_lbl_2.setStyleSheet("")
        self.title_lbl_2.setObjectName("title_lbl_2")

        self.retranslateUi(Admin_window)
        QtCore.QMetaObject.connectSlotsByName(Admin_window)

    def retranslateUi(self, Admin_window):
        _translate = QtCore.QCoreApplication.translate
        Admin_window.setWindowTitle(_translate("Admin_window", "Добро пожаловать в систему"))
        self.title_lbl.setText(_translate("Admin_window", "Каталог товаров"))
        self.add_product_btn.setText(_translate("Admin_window", "Добавить товар"))
        self.create_report_btn.setText(_translate("Admin_window", "Составить отчет"))
        self.add_maneger_btn.setText(_translate("Admin_window", "Добавить менеджера"))
        self.title_lbl_2.setText(_translate("Admin_window", "Сотрудники"))
