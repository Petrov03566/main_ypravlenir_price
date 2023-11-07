import sys
import db
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtCore, QtGui, QtWidgets



class db_client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(db_client=self)
        self.tableView_clin.setModel(db.get_models())
    def setupUi(self, db_client):
        db_client.setObjectName("db_client")
        db_client.resize(715, 419)
        db_client.setStyleSheet("background-color: rgb(245, 194, 17);")
        self.tableView_clin = QtWidgets.QTableView(db_client)
        self.tableView_clin.setGeometry(QtCore.QRect(0, 0, 711, 421))
        self.tableView_clin.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.tableView_clin.setObjectName("tableView_clin")

        self.retranslateUi(db_client)
        QtCore.QMetaObject.connectSlotsByName(db_client)

    def retranslateUi(self, db_client):
        _translate = QtCore.QCoreApplication.translate
        db_client.setWindowTitle(_translate("db_client", "client"))

# if __name__ == "__main__":
#     app =QApplication(sys.argv)
#     window =db_client()
#     window.setupUi
#     window.show()
#     app.exec()
