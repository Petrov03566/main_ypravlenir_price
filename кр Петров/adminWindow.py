from designer.mainWindowAdmin import MainWindowAdmin
from reportWindow import ReportWindow
from addProductWindow import AddPoductWindow
from addManegerWindow import AddManegerWindow
from db import get_model, get_modelUser

class AdminWindow(MainWindowAdmin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableView_product.setModel(get_model())
        self.tableView_user.setModel(get_modelUser())
        self.create_report_btn.clicked.connect(self.create_report_clicked)
        self.add_maneger_btn.clicked.connect(self.add_maneger_clicked)
        self.add_product_btn.clicked.connect(self.add_product_clicked)

    def create_report_clicked(self):
        self.reportWindow = ReportWindow()
        self.reportWindow.show()

    def add_product_clicked(self):
        self.addPeoductWindow = AddPoductWindow()
        self.addPeoductWindow.show()

    def add_maneger_clicked(self):
        self.addManeger = AddManegerWindow()
        self.addManeger.show()