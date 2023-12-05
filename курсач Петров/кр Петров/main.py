import seniorWindow, adminWindow
from PyQt5.QtSql import QSqlQueryModel,QSqlQuery

from db import get_models

# Главное окно Администратора 
class Admin(adminWindow.Ui_Admin_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.push_db.clicked.connect(self.dovabit)
        model = get_models()
        self.tableView.setModel(model)

    def dovabit(self):
        model =QSqlQueryModel()
        q =QSqlQuery(f"INSERT INTO public.cost (name, term ,price) VALUES ('{self.lineEdit.text()}', '{self.lineEdit_2.text()}','{self.lineEdit_4.text()}')")
        q.exec()
        model.clear()
        model.setQuery("product")
        
# Окно Менеджера 
class Senior(seniorWindow.Ui_MainWindow_senior):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        model = get_models()
        self.tableView.setModel(model)
