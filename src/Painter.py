import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, uic
from PyQt5.QtCore import *
# from PyQt5.QtCore import QT
import urllib.request

from_class = uic.loadUiType("../ui/Test9.ui")[0]


class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Draw")

        self.pixmap = QPixmap(self.label.width(), self.label.height())
        self.pixmap.fill(Qt.white)

        self.setMouseTracking(True)
        self.label.setPixmap(self.pixmap)
        # self.drawLine()
        # self.drawPoint()
        # self.drawRect()
        # self.drawEllipse()
        # self.drawText()
        self.x, self.y = None, None

    def wheelEvent(self, event):  # event QWheelEvent
        text = '{0}, {1}'.format(event.angleDelta().x(), event.angleDelta().y())
        self.wheel_label.setText(text)

    
    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton: 
            self.press_label.setText("left")
        if event.buttons() & Qt.RightButton:
            self.press_label.setText("right")

    def mouseMoveEvent(self, event):
        x = event.x() - 10
        y = event.y() - 10

        text = 'x:{0}, y:{1}  global_x:{2}, gloabl_y:{3}'.format(x, y, event.globalX(), event.globalY())
        self.point_label.setText(text)
        self.point_label.adjustSize()
        self.update()
    


    # def mouseMoveEvent(self, event):
    #     x = event.x() - 10
    #     y = event.y() - 10
        
    #     if self.x is None:
    #         self.x = event.x()
    #         self.y = event.y()
    #         return

    #     painter = QPainter(self.label.pixmap())
    #     painter.drawLine(self.x, self.y, x, y)
    #     painter.end()
    #     self.update()

    #     self.x = x
    #     self.y = y

    # def mouseReleaseEvent(self, event):
    #     self.x = None
    #     self.y = None


    def drawText(self):
        painter = QPainter(self.label.pixmap())
        painter.setPen(QPen(Qt.blue, 5, Qt.SolidLine))

        self.font = QFont()
        self.font.setFamily('Times')
        self.font.setBold(True)
        self.font.setPointSize(20)
        painter.setFont(self.font)

        painter.drawText(100, 100, 'This is drawText')
        painter.end

    def drawEllipse(self):
        painter = QPainter(self.label.pixmap())
        painter.setPen(QPen(Qt.red, 5, Qt.SolidLine))
        # painter.setBrush(QBrush(Qt.black))  # brush
        painter.drawEllipse(100, 100, 100, 100)
        painter.end

    def drawRect(self):
        painter = QPainter(self.label.pixmap()) 
        painter.setPen(QPen(Qt.blue, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black))  # brush
        painter.drawRect(100,100, 100, 100)
        painter.end


    def drawPoint(self):
        painter = QPainter(self.label.pixmap())
        painter.setPen(QPen(Qt.red, 20, Qt.SolidLine))
        painter.drawPoint(100, 100)
        painter.end

    def drawLine(self):
        painter = QPainter(self.label.pixmap())

        self.pen = QPen(Qt.red, 5, Qt.SolidLine)
        painter.setPen(self.pen)
        painter.drawLine(100,100,500,100)

        self.pen.setBrush(Qt.blue)
        self.pen.setWidth(10)
        self.pen.setStyle(Qt.DashDotLine)
        painter.setPen(self.pen)
        self.line = QLine(100, 200, 500, 200)
        # painter.drawLine(100, 200, 500, 200) -> # from PyQt5.QtCore import QT 로 사용할때 사용
        painter.drawLine(self.line)

        painter.setPen(QPen(Qt.black, 20, Qt.DotLine))
        self.p1 = QPoint(100, 300)
        self.p2 = QPoint(500, 300)
        painter.drawLine(self.p1, self.p2)
        
        painter.end

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())