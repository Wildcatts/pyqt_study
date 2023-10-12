import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("../ui/Test3_2.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Test3_2")

        self.add_btn.clicked.connect(self.addText)
        self.clear_btn.clicked.connect(self.clear)

        self.ubuntu_btn.clicked.connect(lambda: self.setFont("Ubuntu"))
        self.nanum_btn.clicked.connect(lambda: self.setFont("NanumGothic"))

        self.red_btn.clicked.connect(lambda: self.setTextColor(255, 0, 0))
        self.green_btn.clicked.connect(lambda: self.setTextColor(0, 255, 0))
        self.blue_btn.clicked.connect(lambda: self.setTextColor(0, 0, 255))

        self.set_font_size_btn.clicked.connect(self.setFontSize)
        # self.font_size.textChanged.connect(self.checkDigit)
        self.font_size.returnPressed.connect(self.setFontSize)  # enter key 

        self.font_size.setValidator(QIntValidator())



    def checkDigit(self):
        text = self.font_size.text()
        if (text.isdigit() == False):
            self.font_size.setText(text[:-1])

    def setFontSize(self):
        size = int(self.font_size.text())
        self.output_text.selectAll()  # 전체선택을 위한 옵션
        self.output_text.setFontPointSize(size)
        self.output_text.moveCursor(QTextCursor.End)
             
    def setTextColor(self, r, g, b):
        color = QColor(r, g, b)
        self.output_text.selectAll()  # 전체선택을 위한 옵션
        self.output_text.setTextColor(color)
        self.output_text.moveCursor(QTextCursor.End)

    def addText(self):
        input = self.input_text.toPlainText()
        self.input_text.clear()
        self.output_text.append(input)
    
    def clear(self):
        self.input_text.clear()
        self.output_text.clear()

    def setFont(self, font_name):
        font = QFont(font_name, 11)
        self.output_text.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())