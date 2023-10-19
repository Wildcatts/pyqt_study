# Spin Box
# Slider
# Pix Map

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import urllib.request

from_class = uic.loadUiType("spinbox_slider_pixmap.ui")[0]


class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SpinBox, Slider, PixMap")

        min = self.spinBox.minimum()
        max = self.spinBox.maximum()
        step = self.spinBox.singleStep()
        
        self.editMin.setText(str(min))
        self.editMax.setText(str(max))
        self.editStep.setText(str(step))

        self.slider.setRange(min, max)
        self.slider.setSingleStep(step)

        self.btnApply.clicked.connect(self.Apply)
        self.spinBox.valueChanged.connect(self.ChangeSpinBox)
        self.slider.valueChanged.connect(self.changeSlider)

        self.btnFileOpen.clicked.connect(self.openFile)
        self.btnImgSave.clicked.connect(self.saveImage)

        self.pixmap = QPixmap()
        self.pixmap.load("dog.jpg")
        # url = "https://cdn.royalcanin-weshare-online.io/UCImMmgBaxEApS7LuQnZ/v2/eukanuba-market-image-puppy-beagle?w=5596&h=2317&rect=574,77,1850,1045&auto=compress,enhance"
        # image = urllib.request.urlopen(url).read()
        # self.pixmap.loadFromData(image)

        self.labelPixmap.setPixmap(self.pixmap)
        self.labelPixmap.resize(self.pixmap.width(), self.pixmap.height())
        # self.pixmap = self.pixmap.scaled(self.labelPixmap.width(), self.labelPixmap.height())
        # self.labelPixmap.setPixmap(self.pixmap)

    
    def Apply(self):
        min = self.editMin.text()
        max = self.editMax.text()
        step = self.editStep.text()

        self.spinBox.setRange(int(min), int(max))
        self.spinBox.setSingleStep(int(step))

        self.slider.setRange(int(min), int(max))
        self.slider.setSingleStep(int(step))

    
    def ChangeSpinBox(self):
        actualValue = self.spinBox.value()
        self.labelValue.setText(str(actualValue))
        self.slider.setValue(actualValue)

    
    def changeSlider(self):
        actualValue = self.slider.value()
        self.labelValue2.setText(str(actualValue))
        self.spinBox.setValue(actualValue)


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
                
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())