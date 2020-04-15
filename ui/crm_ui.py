# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *


class CustomerInfo(QWidget):
    def __init__(self):
        super(CustomerInfo, self).__init__()
        self.setWindowTitle(u"客户信息")

        self.init_param()
        self.build_ui()

    def init_param(self):
        pass

    def build_ui(self):
        pass


if __name__ == '__main__':
    print("CRM UI Test here.")
