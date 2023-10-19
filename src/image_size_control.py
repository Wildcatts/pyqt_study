# Spin Box
# Slider
# Pix Map

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import urllib.request

from_class = uic.loadUiType("image_size_control.ui")[0]


class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Image Size Control")

        self.pixmap = QPixmap()
        self.pixmap.load("dog.jpg")
        
        min_width = 1
        min_height = 1
        self.max_width = self.pixmap.width()
        self.max_height = self.pixmap.height()

        self.spinBox_width.setRange(min_width, self.max_width)
        self.spinBox_height.setRange(min_height, self.max_height)
        self.slider_width.setRange(min_width, self.max_width)
        self.slider_height.setRange(min_height, self.max_height)

        step = self.spinBox_width.singleStep()
        self.editStep.setText(str(step))
        
        self.spinBox_height.setSingleStep(step)
        self.slider_width.setSingleStep(step)
        self.slider_height.setSingleStep(step)

        self.spinBox_width.setValue(self.max_width)
        self.spinBox_height.setValue(self.max_height)
        self.slider_width.setValue(self.max_width)
        self.slider_height.setValue(self.max_height)
        
        self.btnApply.clicked.connect(self.Apply)

        self.spinBox_width.valueChanged.connect(lambda: self.ChangeSpinBox(self.pixmap))
        self.spinBox_height.valueChanged.connect(lambda: self.ChangeSpinBox(self.pixmap))
        
        self.slider_width.valueChanged.connect(lambda: self.changeSlider(self.pixmap))
        self.slider_height.valueChanged.connect(lambda: self.changeSlider(self.pixmap))

        self.btnFileOpen.clicked.connect(self.openFile)
        self.btnImgSave.clicked.connect(self.saveImage)

        self.labelPixmap.setPixmap(self.pixmap)
        self.labelPixmap.resize(self.pixmap.width(), self.pixmap.height())

    
    def Apply(self):
        step = self.editStep.text()
        self.spinBox_width.setSingleStep(int(step))
        self.spinBox_height.setSingleStep(int(step))
        self.slider_width.setSingleStep(int(step))
        self.slider_height.setSingleStep(int(step))

    
    def ChangeSpinBox(self, pixmap):
        actualValue_width = self.spinBox_width.value()
        actualValue_height = self.spinBox_height.value()
        
        self.labelValue_width.setText(str(actualValue_width))
        self.labelValue_height.setText(str(actualValue_height))

        self.slider_width.setValue(actualValue_width)
        self.slider_height.setValue(actualValue_height)

        pixmap = pixmap.scaled(actualValue_width, actualValue_height)
        self.labelPixmap.resize(pixmap.width(), pixmap.height())
        self.labelPixmap.setPixmap(pixmap)

    
    def changeSlider(self, pixmap):
        actualValue_width = self.slider_width.value()
        actualValue_height = self.slider_height.value()

        self.labelValue_width_2.setText(str(actualValue_width))
        self.labelValue_height_2.setText(str(actualValue_height))

        self.spinBox_width.setValue(actualValue_width)
        self.spinBox_height.setValue(actualValue_height)

        pixmap = self.pixmap.scaled(actualValue_width, actualValue_height)
        self.labelPixmap.resize(pixmap.width(), pixmap.height())
        self.labelPixmap.setPixmap(pixmap)


    def saveImage(self):
        name = QFileDialog.getSaveFileName(self, "Save Image", "./")
        if name[0]:
            self.pixmap.save(name[0])
    
    
    def openFile(self):
        name = QFileDialog.getOpenFileName(self, "Upload Image", "./")

        if name[0]:
            self.pixmap.load(name[0])
            self.labelPixmap.setPixmap(self.pixmap)
            self.labelPixmap.resize(self.pixmap.width(), self.pixmap.height())

            self.spinBox_width.setValue(self.pixmap.width())
            self.spinBox_height.setValue(self.pixmap.height())
            self.slider_width.setValue(self.pixmap.width())
            self.slider_height.setValue(self.pixmap.height())
                
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())