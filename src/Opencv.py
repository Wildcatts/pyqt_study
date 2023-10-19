import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import cv2, imutils
import time
import datetime
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from_class = uic.loadUiType("../ui/opencv.ui")[0]

class Camera(QThread):
    update = pyqtSignal()

    def __init__(self, sec=0, parent=None) -> None:
        super().__init__()
        self.main = parent
        self.running = True

    def run(self):
        count = 0
        while self.running == True:
            self.update.emit()
            time.sleep(0.05)

    def stop(self):
        self.running = False

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Opencv")

        self.isCameraOn = False
        self.isRecOn = False
        self.rec_btn.hide()
        self.capture_btn.hide()

        self.pixmap = QPixmap()

        self.camera = Camera(self)
        self.camera.daemon = True

        self.record = Camera(self)
        self.record.daemon = True

        self.count = 0
        self.video_capture = None

        self.open_btn.clicked.connect(self.openFile)
        self.camera_btn.clicked.connect(self.clickCamera)
        self.camera.update.connect(self.updateCamera)
        self.rec_btn.clicked.connect(self.clickRecord)
        self.record.update.connect(self.updateRecording)
        self.capture_btn.clicked.connect(self.capture)

    def capture(self):
        self.now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        capturename = self.now + '.png'
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(capturename, self.image)

    def updateRecording(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        self.writer.write(self.image)
        self.label_2.setText(str(self.count))
        self.count += 1


    def clickRecord(self):
        if self.isRecOn == False:
            self.rec_btn.setText('Rec Off')
            self.isRecOn = True

            self.recordingStart()
        else:
            self.rec_btn.setText('Rec On')
            self.isRecOn = False

            self.recordingStop()

    def recordingStart(self):
        self.record.running = True
        self.record.start()

        self.now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        videoname = self.now + '.avi'
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')

        w = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.writer = cv2.VideoWriter(videoname, self.fourcc, 20.0, (w, h))

    def recordingStop(self):
        self.record.running = False
        
        if self.isRecOn == True:
            self.writer.relese()


    def updateCamera(self):
        retal, image = self.video.read()
        if retal:
            # self.image = cv2.cvtColor(image, cv2.IMREAD_COLOR)
            self.image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            h, w, c = self.image.shape
            qimage = QImage(self.image.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)


    def clickCamera(self):
        if self.isCameraOn == False:
            self.camera_btn.setText('Camera Off')
            self.isCameraOn = True
            self.rec_btn.show()
            self.capture_btn.show()

            self.cameraStart()
        else:
            self.camera_btn.setText('Camera On')
            self.isCameraOn = False
            self.rec_btn.hide()
            self.capture_btn.hide()

            self.cameraStop()
            self.recordingStop()

    def cameraStart(self):
        self.camera.running = True
        self.camera.start()
        self.video = cv2.VideoCapture(-1)

    def cameraStop(self):
        self.camera.running = False
        self.count = 0
        self.video.release

    def openFile(self):
        file,_ = QFileDialog.getOpenFileName(filter='Image (*.*)')

        if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff")):
            image = cv2.imread(file)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            h, w, c = image.shape
            qimage = QImage(image.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)
        else:
            self.video_capture = cv2.VideoCapture(file)

            if self.video_capture.isOpened():
                self.playVideo()
    
    def playVideo(self):
        while True:
            ret, frame = self.video_capture.read()
            
            if not ret:
                break
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

            self.pixmap = QPixmap.fromImage(q_image)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)
            QApplication.processEvents()

            time.sleep(0.05)  # 저장된 동영상에 맞게 setting

        self.video_capture.release()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())