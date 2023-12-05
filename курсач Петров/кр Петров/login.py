import sys
import loginWindow
from main import Admin, Senior
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel, QSqlTableModel
from PyQt5.QtWidgets import QApplication
from db import connect

# авторизация 
class Avtoriza(loginWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_auth.clicked.connect(self.open)
        connect()

    def open(self):
        if self.lineEdit.text() == 'admin' and self.lineEdit_2.text() == 'admin':
            self.admin_window = Admin()
            self.admin_window.show()
            self.close()

        if self.lineEdit.text() == 'senior' and self.lineEdit_2.text() == 'senior':
            self.senior_window = Senior()
            self.senior_window.show()
            self.close()
    def user(self):
        model2 = QSqlQueryModel()
        model2.setQuery("SELECT * FROM public.user WHERE login = 'admin',password = 'admin")
        
    
            
app = QApplication(sys.argv)
window = Avtoriza()
window.show()
app.exec()