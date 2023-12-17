from report import ReportWindowDesign
from db import get_product_count

class ReportWindow(ReportWindowDesign):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        count = get_product_count()
        print(count.first())
