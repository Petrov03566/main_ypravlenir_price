from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(334, 293)
        MainWindow.setStyleSheet("background-color: rgb(229, 165, 10);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_auth = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_auth.setGeometry(QtCore.QRect(110, 160, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_auth.setFont(font)
        self.pushButton_auth.setObjectName("pushButton_auth")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 40, 221, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"border-radius: 20px;\n"
"border: rgb(255, 163, 72);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 100, 221, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"border-radius: 20px;\n"
"border: rgb(0,0,0);\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 59, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_auth_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_auth_3.setGeometry(QtCore.QRect(110, 210, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_auth_3.setFont(font)
        self.pushButton_auth_3.setObjectName("pushButton_auth_3")
        self.pushButton_auth.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton_auth_3.raise_()
        self.lineEdit_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "auth"))
        self.pushButton_auth.setText(_translate("MainWindow", "вход"))
        self.label.setText(_translate("MainWindow", "логин"))
        self.label_2.setText(_translate("MainWindow", "пароль"))
        self.pushButton_auth_3.setText(_translate("MainWindow", "Выход"))
