# База данных имя таблица продукт 
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel, QSqlTableModel
from PyQt5.QtCore import Qt

def connect_to_db():
    db = QSqlDatabase.addDatabase('QPSQL')
    db.setHostName('localhost')
    db.setPort(5432)
    db.setDatabaseName('cost')
    db.setUserName('postgres')
    db.setPassword('student')
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

def get_modelUser():
    modelUser = QSqlTableModel()
    modelUser.setTable("user")
    modelUser.select()
    modelUser.removeColumn(0)
    modelUser.removeColumn(5)
    modelUser.setHeaderData(0, Qt.Orientation.Horizontal, "имя")
    modelUser.setHeaderData(1, Qt.Orientation.Horizontal, "фамилия")
    modelUser.setHeaderData(2, Qt.Orientation.Horizontal, "отчество")
    modelUser.setHeaderData(3, Qt.Orientation.Horizontal, "логин")
    modelUser.setHeaderData(4, Qt.Orientation.Horizontal, "пароль")
    return modelUser

def addProduct(name, quantity, price):
    queryProduct = QSqlQuery()
    queryProduct.exec(f"INSERT INTO public.product (name, quantity, price) VALUES ('{name}', '{quantity}', '{price}')")

def addUser(name, sname, tname, login, psw):
    queryUser = QSqlQuery()
    queryUser.exec(f"INSERT INTO public.product (name, secondname, thirstname, login, password, role_id) VALUES ('{name}', '{sname}', '{tname}', '{login}', '{psw}', '1')")

def get_product_count():
    query = QSqlQuery()
    query.exec("SELECT * FROM public.product")
    print(query.isActive())
    query.first()
    j = 0
    i = []
    while True:
        if query.next() == False:
            break
        else:
            i[j] = str(query.value(j))
            j += 1
    sum = 0
    for x in range(len(i)):
        sum += i[x]
    return (len(i), sum)

# def product(name, term, price):
#     model =QSqlQueryModel()
#     q =QSqlQuery(f"INSERT INTO public.cost (name, term ,price) VALUES ('{name}', '{term}','{price}')")
#     q.exec()
#     model.clear()
#     model.setQuery("product")