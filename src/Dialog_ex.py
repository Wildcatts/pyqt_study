import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import mysql.connector

from_class = uic.loadUiType("../ui/Test7_1.ui")[0]

local = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123123",
        database = "armbase"
    )

cursor_sex = local.cursor(buffered=True)
cursor_job = local.cursor(buffered=True)
cursor_agency = local.cursor(buffered=True)

sql_sex = "select sex from celeb;"
sql_job = "select job_title from celeb;"
sql_agency = "select agency from celeb;"

cursor_sex.execute(sql_sex)
cursor_job.execute(sql_job)
cursor_agency.execute(sql_agency)
result_sex = cursor_sex.fetchall()
result_job = cursor_job.fetchall()
result_agency = cursor_agency.fetchall()
print(result_job)

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Dialog")

        self.sex_cb.addItem("ALL")
        self.sex_cb.addItem("Male")
        self.sex_cb.addItem("Female")

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # for row in result:
        #     self.textBrowser.setText()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())