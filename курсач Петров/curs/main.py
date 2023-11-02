import sys
import seniorMain

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(296, 320)
        MainWindow.setStyleSheet("background-color:  rgb(245, 194, 17)")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_auth = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_auth.setGeometry(QtCore.QRect(70, 250, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_auth.setFont(font)
        self.pushButton_auth.setObjectName("pushButton_auth")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 70, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 170, 221, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 59, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 71, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.pushButton_auth.clicked.connect(self.btn_auth)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "auth"))
        self.pushButton_auth.setText(_translate("MainWindow", "вход"))
        self.label.setText(_translate("MainWindow", "логин"))
        self.label_2.setText(_translate("MainWindow", "пароль"))

    def btn_auth(self):
        if self.lineEdit.text() == '1' and self.lineEdit_2.text() == '1':
            # self.window_test = TestWindow()
            # self.window_test.show()
            pass
        if self.lineEdit.text() =='2' and self.lineEdit_2.text() =='2':
            self.senior =seniorMain.MainSenior()
            self.senior.show()

if __name__ == "__main__":
    app =QApplication(sys.argv)
    window =Login()
    window.show()
    app.exec()