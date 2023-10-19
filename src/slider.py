import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from datetime import datetime

from_class = uic.loadUiType("slider.ui")[0]


class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Slider")

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

    
    def Apply(self):
        min = self.editMin.text()
        max = self.editMax.text()
        step = self.editStep.text()

        self.spinBox.setRange(int(min), int(max))
        self.spinBox.setSingleStep(int(step))

        self.slider.setRange(int(min), int(max))
        self.slider.setSingleStep(int(step))
        self.slider.valueChanged.connect(self.changeSlider)

    
    def ChangeSpinBox(self):
        actualValue = self.spinBox.value()
        self.labelValue.setText(str(actualValue))
        self.slider.setValue(actualValue)

    
    def changeSlider(self):
        actualValue = self.slider.value()
        self.labelValue2.setText(str(actualValue))
        self.spinBox.setValue(actualValue)
        





    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())