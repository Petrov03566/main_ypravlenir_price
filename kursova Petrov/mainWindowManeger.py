# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowManeger.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindowManeger(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow_senior):
        MainWindow_senior.setObjectName("MainWindow_senior")
        MainWindow_senior.resize(533, 505)
        MainWindow_senior.setStyleSheet("background-color: rgb(245, 194, 17);")
        self.centralwidget = QtWidgets.QWidget(MainWindow_senior)
        self.centralwidget.setObjectName("centralwidget")
        self.create_report_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_report_btn.setGeometry(QtCore.QRect(130, 410, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.create_report_btn.setFont(font)
        self.create_report_btn.setObjectName("create_report_btn")
        self.title_lbl = QtWidgets.QLabel(self.centralwidget)
        self.title_lbl.setGeometry(QtCore.QRect(170, 10, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title_lbl.setFont(font)
        self.title_lbl.setStyleSheet("")
        self.title_lbl.setObjectName("title_lbl")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 80, 511, 301))
        self.tableView.setStyleSheet("background-color: rgb(233, 241, 250);")
        self.tableView.setObjectName("tableView")
        MainWindow_senior.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_senior)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_senior)

    def retranslateUi(self, MainWindow_senior):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_senior.setWindowTitle(_translate("MainWindow_senior", "MainWindow"))
        self.create_report_btn.setText(_translate("MainWindow_senior", "Составить отчет"))
        self.title_lbl.setText(_translate("MainWindow_senior", "Каталог товаров"))
