# -*- coding: utf-8 -*-
import sys

from PySide2.QtCore import QUrl
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtMultimediaWidgets import QGraphicsVideoItem, QVideoWidget
from PySide2.QtWidgets import *


class MainView(QGraphicsView):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)


class MyApp(QWidget):
    def __int__(self):
        super(MyApp, self).__init__()

        self.master_layout = QVBoxLayout()

        player = QMediaPlayer()
        item = QGraphicsVideoItem()
        player.setVideoOutput(item)
        player.setMedia((QUrl("D:/test/1.mov")))
        graphicsView = MainView()
        graphicsView.scene().addItem(item)
        graphicsView.show()

        self.master_layout.addWidget(graphicsView)
        self.setLayout(self.master_layout)
        player.play()


def test():
    url = QUrl.fromLocalFile("D:/test/1.mov")
    content = QMediaContent(url)
    player = QMediaPlayer()
    player.setMedia(content)
    # player.setVolume(Sound_level)
    player.play()


def test2():
    url = QUrl.fromLocalFile("D:/test/2.mp4")
    content = QMediaContent(url)
    player = QMediaPlayer()
    vw = QVideoWidget()
    vw.show()
    player.play()
    player.setVideoOutput(vw)
    player.setMedia(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # window = MyApp()
    # window.show()
    test2()
    sys.exit(app.exec_())
