from designer.report import ReportWindowDesign
from db import get_product_count

class ReportWindow(ReportWindowDesign):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        count = get_product_count()
        self.label.setText(f"Общее количество товаров: {count[0]}")
        self.label_2.setText(f"Общее стоимость товаров: {count[1]}")
