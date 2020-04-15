from PySide2.QtMultimedia import QCamera
from PySide2.QtMultimediaWidgets import QCameraViewfinder
import time

if __name__ == '__main__':
    camera = QCamera
    viewfinder = QCameraViewfinder()
    viewfinder.show()
    camera.setViewfinder(viewfinder)
    imageCapture = QCameraViewfinder(camera)
    camera.setCaptureMode(QCamera.CaptureStillImage)
    camera.start()
    time.sleep(10)
    camera.stop()
    imageCapture.saveGeometry()

