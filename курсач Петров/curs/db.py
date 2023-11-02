from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel, QSqlTableModel
from PyQt5.QtCore import Qt


db = QSqlDatabase.addDatabase('QPSQL')
db.setHostName('localhost')
db.setPort(5432)
db.setDatabaseName('cost')
db.setUserName('postgres')
db.setPassword('student')
db.open()
    
def get_models():
    model =QSqlQueryModel()
    model.setQuery("SELECT public.product.id, name, term, price, discounts.procent FROM public.product INNER JOIN public.discounts ON public.product.id = discounts.product_id")
    model.setHeaderData(0, Qt.Orientation.Horizontal, "номер")
    model.setHeaderData(1, Qt.Orientation.Horizontal, "имя")
    model.setHeaderData(2, Qt.Orientation.Horizontal, "cрок годности")
    model.setHeaderData(3, Qt.Orientation.Horizontal, "цена")
    model.setHeaderData(4, Qt.Orientation.Horizontal, "скидка в %")
    return model

def skidka_1(proce ,nomer_tovar):
    mod = QSqlQuery()
    mod.exec(f"UPDATE public.discounts SET procent = {proce} WHERE product_id = {nomer_tovar}")

def change_price(number, number2):
    mod2 = QSqlQuery()
    mod2.exec(f"UPDATE public.product SET price ={number} WHERE id = {number2}")