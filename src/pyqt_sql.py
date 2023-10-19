import mysql.connector
# import pandas as pd
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from datetime import datetime

from_class = uic.loadUiType("PyQt_sql.ui")[0]


class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PyQt_sql")

        self.remote = mysql.connector.connect(
            host = 'database-1.cccbm3nnjzrq.ap-northeast-2.rds.amazonaws.com',
            port = 3306,
            user = 'admin',
            password = 'khe!301105',
            database = 'amrbase'
        )

        cursor = self.remote.cursor(buffered=True)

        self.cbSex.addItem("All")
        cursor.execute("SELECT DISTINCT SEX FROM celeb")
        result = cursor.fetchall()
        for res in result:
            self.cbSex.addItem(res[0])

        self.cbJobTitle.addItem("All")
        self.cbJobTitle.addItem("가수")
        self.cbJobTitle.addItem("텔런트")
        self.cbJobTitle.addItem("영화배우")
        self.cbJobTitle.addItem("MC")
        self.cbJobTitle.addItem("개그맨")
        self.cbJobTitle.addItem("모델")

        self.cbAgency.addItem("All")
        self.cbAgency.addItem("EDAM엔터테이먼트")
        self.cbAgency.addItem("울림엔터테이먼트")
        self.cbAgency.addItem("나무엑터스")
        self.cbAgency.addItem("YG엔터테인먼트")
        self.cbAgency.addItem("안테나")


        self.cbSex.addItem("All")
        self.cbJobTitle.addItem("All")
        self.cbAgency.addItem("All")

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.pushButton.clicked.connect(self.Search)

        
    
    def Search(self):
        birthday_start = self.dateEdit_start.text().replace(".", "")
        birthday_end = self.dateEdit_end.text().replace(".", "")
        sex = self.cbSex.currentText()
        jobtitle = self.cbJobTitle.currentText()
        agency = self.cbAgency.currentText()
        
        cursor = self.remote.cursor(buffered=True)
        
        query = "SELECT * FROM celeb WHERE "
        
        birth_query = "BIRTHDAY BETWEEN " + birthday_start + " and " + birthday_end

        if sex != "All":
            if sex == "F":
                sex_qeury = "SEX = 'F'"
            else:
                sex_qeury = "SEX = 'F'"
        else:
            sex_qeury = ""

        if jobtitle != "All":
            if jobtitle == "가수": job_qeury = "JOB_TITLE LIKE '%가수%'"
            elif jobtitle == "텔런트": job_qeury = "JOB_TITLE LIKE '%텔런트%'"
            elif jobtitle == "영화배우": job_qeury = "JOB_TITLE LIKE '%영화배우%'"
            elif jobtitle == "MC": job_qeury = "JOB_TITLE LIKE '%MC%'"
            elif jobtitle == "개그맨": job_qeury = "JOB_TITLE LIKE '%개그맨%'"
            else: job_qeury = "JOB_TITLE LIKE '%가수%'"
        else:
            job_qeury = ""

        if agency != "All":
            if agency == "EDAM엔터테이먼트": agency_query = "AGENCY = 'EDAM엔터테이먼트'"
            elif agency == "울림엔터테이먼트":agency_query = "AGENCY = '울림엔터테이먼트'"
            elif agency == "나무엑터스":agency_query = "AGENCY = '나무엑터스'"
            elif agency == "YG엔터테인먼트":agency_query = "AGENCY = 'YG엔터테인먼트'"
            else: agency = "AGENCY = '안테나'"
        else:
            agency_query = ""

        cursor.execute(query + birth_query + " and " + sex_qeury + " and " + job_qeury + " and " + agency_query)

        result = cursor.fetchall()
        for res in result:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            
            birth = res[2].strftime("%Y-%m-%d")
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(res[0])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(res[1]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(birth))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(res[3])))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(res[4]))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(res[5]))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(res[6]))
        
        self.cbSex.setCurrentText("All")
        self.cbJobTitle.setCurrentText("All")
        self.cbAgency.setCurrentText("All")


    
        


if __name__ == "__main__":
    
    
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())

    # remote.close()

    


