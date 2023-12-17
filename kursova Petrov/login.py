import sys
import loginWindow 
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication
from db import connect_to_db
from adminWindow import AdminWindow
from manegerWindow import ManegerWindow

# авторизация 
class Login(loginWindow.LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_auth.clicked.connect(self.login)
        connect_to_db()

    def login(self):
        us = self.query_login()
        if us.first():
            if us.value(6) == 1:
                self.adminWimndow = AdminWindow()
                self.adminWimndow.show()
                self.close()
                

            elif us.value(6) == 2:
                self.adminWimndow = ManegerWindow()
                self.adminWimndow.show()
                self.close()

    def query_login(self):
        model2 = QSqlQuery()
        model2.exec(f"SELECT * FROM public.user \
        WHERE login = '{self.lineEdit.text()}' AND \
        psw = '{self.lineEdit_2.text()}'")
        return model2
    
            
app = QApplication(sys.argv)
window = Login()
window.show()
app.exec()