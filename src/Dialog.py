import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("../ui/Test7.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Dialog")

        self.gender_cb.addItem("Man")
        self.gender_cb.addItem("Woman")
        self.gender_cb.addItem("Other")

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.add_btn.clicked.connect(self.add)

    def add(self):
        name_edit = self.name_edit.text()

        if name_edit != "":
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(self.name_edit.text()))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(self.gender_cb.currentText()))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(self.birthday_edit.text()))
        else:
            QMessageBox.warning(self, 'Wrong Insert', 'Please input right name')
            self.lineEdit.clear()

        self.name_edit.clear()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())