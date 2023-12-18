from designer.addManeger import AddManeger
from db import addUser

class AddManegerWindow(AddManeger):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_product_btn_2.clicked.connect(self.add_maneger_clicked)

    def add_maneger_clicked(self):
        addUser(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text())