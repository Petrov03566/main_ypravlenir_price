# База данных имя таблица продукт 
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel, QSqlTableModel
from PyQt5.QtCore import Qt
def connect_to_db():
    db = QSqlDatabase.addDatabase('QPSQL')
    db.setHostName('localhost')
    db.setPort(5432)
    db.setDatabaseName('cost')
    db.setUserName('postgres')
    db.setPassword('Doctor')
    db.open()

def get_model():
    model = QSqlTableModel()
    model.setTable("product")
    model.select()
    model.setHeaderData(0, Qt.Orientation.Horizontal, "номер")
    model.setHeaderData(1, Qt.Orientation.Horizontal, "имя")
    model.setHeaderData(2, Qt.Orientation.Horizontal, "количество")
    model.setHeaderData(3, Qt.Orientation.Horizontal, "цена")
    return model

def get_product_count():
    query = QSqlQuery("SELECT COUNT(*) FROM public.product")
    query.exec()
    return query


# def product(name, term, price):
#     model =QSqlQueryModel()
#     q =QSqlQuery(f"INSERT INTO public.cost (name, term ,price) VALUES ('{name}', '{term}','{price}')")
#     q.exec()
#     model.clear()
#     model.setQuery("product")