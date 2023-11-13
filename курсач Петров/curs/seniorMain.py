from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import db
import add_skidka
import change_price

class MainSenior(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table.setModel(db.get_models())

    def setupUi(self, MainWindow_senior):
        MainWindow_senior.setObjectName("MainWindow_senior")
        MainWindow_senior.resize(932, 392)
        MainWindow_senior.setStyleSheet("background-color: rgb(245, 194, 17);")
        self.centralwidget = QtWidgets.QWidget(MainWindow_senior)
        self.centralwidget.setObjectName("centralwidget")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(40, 280, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.clicked_add)
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(290, 20, 519, 341))
        self.table.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.table.setObjectName("table")
        self.change_tovar = QtWidgets.QPushButton(self.centralwidget)
        self.change_tovar.setGeometry(QtCore.QRect(40, 220, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.change_tovar.setFont(font)
        self.change_tovar.setObjectName("change_tovar")
        self.change_tovar.clicked.connect(self.update_tovar)
        MainWindow_senior.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_senior)
        self.statusbar.setObjectName("statusbar")
        MainWindow_senior.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_senior)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_senior)

    def retranslateUi(self, MainWindow_senior):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_senior.setWindowTitle(_translate("MainWindow_senior", "MainWindow"))
        self.add_btn.setText(_translate("MainWindow_senior", "добавить скидку"))
        self.change_tovar.setText(_translate("MainWindow_senior", "изменить цену"))

    def clicked_add(self):
        self.mod =add_skidka.Skidka(self.update)
        self.mod.show()

    def update(self):
        self.table.setModel(db.get_models())

    def update_tovar(self):
        self.change = change_price.Ui_Form(update=self.update)
        self.change.show()

    


if __name__ == "__main__":
    app =QtWidgets.QApplication(sys.argv)
    window =MainSenior()
    window.show()
    app.exec()