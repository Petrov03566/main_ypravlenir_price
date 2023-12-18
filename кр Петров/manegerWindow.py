from designer.mainWindowManeger import MainWindowManeger
from db import get_model
from reportWindow import ReportWindow

class ManegerWindow(MainWindowManeger):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableView.setModel(get_model())
        self.create_report_btn.clicked.connect(self.create_report_clicked)

    def create_report_clicked(self):
        self.reportWindow = ReportWindow()
        self.reportWindow.show()