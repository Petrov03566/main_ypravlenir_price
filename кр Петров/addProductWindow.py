from designer.addProduct import AppProduct
from db import addProduct

class AddPoductWindow(AppProduct):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_product_btn.clicked.connect(self.add_product_clicked)

    def add_product_clicked(self):
        addProduct(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text())