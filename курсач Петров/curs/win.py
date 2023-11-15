import sys
import adn2
# import db  
import add_skidka
import change_price
import client
import main
import seniorMain
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel, QSqlTableModel
from PyQt5.QtCore import Qt


class Avtoriza(main.MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_auth.clicked.connect(self.open)
        self.show()

    def open(self):
        if self.lineEdit.text() == '1' and self.lineEdit_2.text() == '1':
            self.Admin_window =Admin()
            self.Admin_window.show()
            
        if self.lineEdit.text() =='2' and self.lineEdit_2.text() =='2':
            self.senior =seniorMain.MainSenior()
            self.senior.show()
        if self.lineEdit.text() =='3' and self.lineEdit_2.text() =='3':
            self.client =client.db_client()
            self.client.show()

        
        
class Admin(adn2.Admin_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    

        db = QSqlDatabase.addDatabase('QPSQL')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setDatabaseName('cost')
        db.setUserName('postgres')
        db.setPassword('student')
        db.open()
        queru =QSqlQuery()
        sql ="SELECT * FROM public.cost"
        queru.exec(sql)
        queru.first()


        if queru.isActive():
            print('ok')

        else:
            print('no')
        stm =QSqlTableModel(parent=self.TableView)
        stm.setTable('cost')
        stm.select()
        self.TableView.setModel(stm)
        self.TableView.setColumnHidden(0, True)
        self.table =self.TableView.viewport().width()
        columnCount =self.TableView.model().columnCount()
        columnWidth =int((self.table * 1.25) /columnCount)

        for column in range(columnCount):
            self.TableView.setColumnWidth(column, columnWidth)
 
        self.TableView.clicked.connect(self.)   
    
    # def get_models2():
    #     model =QSqlQueryModel()
    #     model.setQuery("SELECT public.product.id, name, term, price, discounts.procent FROM public.product INNER JOIN public.discounts ON public.product.id = discounts.product_id")
    #     model.setHeaderData(0, Qt.Orientation.Horizontal, "номер")
    #     model.setHeaderData(1, Qt.Orientation.Horizontal, "имя")
    #     model.setHeaderData(2, Qt.Orientation.Horizontal, "cрок годности")
    #     model.setHeaderData(3, Qt.Orientation.Horizontal, "цена")
    #     model.setHeaderData(4, Qt.Orientation.Horizontal, "скидка в %")
    #     return model

    # def skidka_1(proce ,nomer_tovar):
    #     mod = QSqlQuery()
    #     mod.exec(f"UPDATE public.discounts SET procent = {proce} WHERE product_id = {nomer_tovar}")

    # def change_price(number, number2):
    #     mod2 = QSqlQuery()
    #     mod2.exec(f"UPDATE public.product SET price ={number} WHERE id = {number2}")

    # def spisok_tovar(name, price , term):
    #     mod3 = QSqlQuery()
    #     mod3.exec(f"INSERT INTO public.product (name, term, price) VALUES ('{name}','{term}','{price}' )")
    #     idPriduct = mod3.lastInsertId()
    #     mod3.clear()
    #     mod3.exec(f"INSERT INTO public.discounts (procent, product_id) VALUES ('0', '{idPriduct}')")
    
    


        

  



app = QApplication(sys.argv)
window = Avtoriza()
window.show()  # Corrected method call
app.exec()