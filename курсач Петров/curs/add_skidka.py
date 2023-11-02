
import sys
import db
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


class Skidka(QtWidgets.QWidget):
    def __init__(self, update):
        super().__init__()
        self.upd = update
        self.setupUi(Form = self)
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

        self.add_btn.clicked.connect(self.add_btn_click)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить скидку"))
        self.number_lbl1.setText(_translate("Form", "номер товара"))
        self.lineEdit.setText(_translate("Form", "0"))
        self.skidki_lbl.setText(_translate("Form", "размер скидки"))
        self.add_btn.setText(_translate("Form", "добавить"))

    def add_btn_click(self):
        db.skidka_1(proce=self.spinBox.value(), nomer_tovar=self.lineEdit.text())
        self.upd()
        self.close()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Skidka()
    window.show()
    app.exec()