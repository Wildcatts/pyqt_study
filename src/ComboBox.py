import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from datetime import datetime

from_class = uic.loadUiType("../ui/Test6.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ComboBox")

        for year in range(1900, 2023 + 1):
            self.year_cb.addItem(str(year))

        for month in range(1, 12 + 1):
            self.month_cb.addItem(str(month))

        for day in range(1, 31 + 1):
            self.day_cb.addItem(str(day))

        self.year_cb.setCurrentText(str(1990))
        self.month_cb.setCurrentText(str(1))
        self.day_cb.setCurrentText(str(1))

        self.printBirthday()

        self.year_cb.currentIndexChanged.connect(self.printBirthday)
        self.month_cb.currentIndexChanged.connect(self.printBirthday)
        self.day_cb.currentIndexChanged.connect(self.printBirthday)

        self.calendarWidget.clicked.connect(self.selectDate)

    def selectDate(self):
        date = self.calendarWidget.selectedDate()
        year = date.toString('yyyy')
        month = date.toString('M')
        day = date.toString('d')

        self.year_cb.setCurrentText(year)
        self.month_cb.setCurrentText(month)
        self.day_cb.setCurrentText(day)

        date_obj = datetime.strptime(year + month + day, "%Y%m%d")
        self.lineEdit.setText(date_obj.strftime("%Y-%m-%d"))

    def printBirthday(self):
        year = self.year_cb.currentText()
        month = self.month_cb.currentText()
        day = self.day_cb.currentText()

        date_obj = datetime.strptime(year + month.zfill(2) + day.zfill(2), "%Y%m%d")
        self.lineEdit.setText(date_obj.strftime("%Y-%m-%d"))
        # self.lineEdit.setText(birthday.strftime("%Y %m %d"))




if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())