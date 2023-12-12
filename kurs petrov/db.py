# База данных имя таблица продукт 
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel, QSqlTableModel
from PyQt5.QtCore import Qt

def connect():
    db = QSqlDatabase.addDatabase('QPSQL')
    db.setHostName('localhost')
    db.setPort(5432)
    db.setDatabaseName('cost')
    db.setUserName('postgres')
    db.setPassword('Doctor')
    db.open()

def get_models():
    model = QSqlQueryModel()
    model.setQuery("SELECT public.product.id, name, term, price, discounts.procent FROM public.product INNER JOIN public.discounts ON public.product.id = discounts.product_id")
    model.setHeaderData(0, Qt.Orientation.Horizontal, "номер")
    model.setHeaderData(1, Qt.Orientation.Horizontal, "имя")
    model.setHeaderData(2, Qt.Orientation.Horizontal, "cрок годности")
    model.setHeaderData(3, Qt.Orientation.Horizontal, "цена")
    model.setHeaderData(4, Qt.Orientation.Horizontal, "скидка в %")
    return model

# def product(name, term, price):
#     model =QSqlQueryModel()
#     q =QSqlQuery(f"INSERT INTO public.cost (name, term ,price) VALUES ('{name}', '{term}','{price}')")
#     q.exec()
#     model.clear()
#     model.setQuery("product")