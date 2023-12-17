from mainWindowAdmin import MainWindowAdmin
from db import get_model

class AdminWindow(MainWindowAdmin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableView.setModel(get_model())