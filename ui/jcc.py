import sys

from PySide2.QtWidgets import *

class JCCMain(QWidget):
    def __init__(self):
        super(JCCMain, self).__init__()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JCCMain()
    window.show()
    sys.exit(app.exec_())


