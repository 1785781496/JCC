# -*- coding: utf-8 -*-
import sys

from PySide2.QtWidgets import QWidget, QApplication


class BaseWindow(QWidget):
    def __init__(self):
        super(BaseWindow, self).__init__()
        self.left_list = []


class DAMWidget(BaseWindow):
    def __init__(self):
        super(DAMWidget, self).__init__()
        self.setWindowTitle("DAM")


if __name__ == '__main__':
    print("DAM Browser Begins.")
    app = QApplication(sys.argv)
    window = DAMWidget()
    window.show()
    sys.exit(app.exec_())
