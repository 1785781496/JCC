# -*- coding: utf-8 -*-
import sys

from PySide2.QtWidgets import *
from crm.crm_data import *


class CRMWindow(QWidget):
    def __init__(self):
        super(CRMWindow, self).__init__()
        self.setWindowTitle(u"CRM")
        self.resize(1024, 512)
        self.build_ui()

    def build_ui(self):
        left_layout = QHBoxLayout()
        list_widget = QListWidget()
        list_widget.addItems(get_customer_list())
        list_widget.currentItemChanged.connect(self.change)
        left_layout.addWidget(list_widget)

        mid_layout = QVBoxLayout()
        mid_top_layout = QVBoxLayout()
        self.lable_customer = QLabel()
        lable_contract = QLabel(u"合同：结束日期/到期提醒")
        lable_issue_number = QLabel(u"问题：已解决/未解决")
        lable_dev_number = QLabel(u"开发：已完成/未完成")
        lable_update_number = QLabel(u"更新：当前版本/最新版本")
        mid_top_layout.addWidget(self.lable_customer)
        mid_top_layout.addWidget(lable_contract)
        mid_top_layout.addWidget(lable_issue_number)
        mid_top_layout.addWidget(lable_dev_number)
        mid_top_layout.addWidget(lable_update_number)
        list_widget_info = QListWidget()
        list_widget_info.addItems(get_info_list())
        list_widget_info.currentItemChanged.connect(self.change_info)
        mid_layout.addLayout(mid_top_layout, 40)
        mid_layout.addWidget(list_widget_info, 60)

        right_layout = QHBoxLayout()
        self.lable_detail = QLabel()
        right_layout.addWidget(self.lable_detail)

        master_layout = QHBoxLayout()
        master_layout.addLayout(left_layout, 10)
        master_layout.addLayout(mid_layout, 30)
        master_layout.addLayout(right_layout, 60)

        self.setLayout(master_layout)

    def change(self, event):
        self.lable_customer.setText(event.text())

    def change_info(self, event):
        self.lable_detail.setText(event.text())


if __name__ == '__main__':
    print("CRM starts.")
    app = QApplication(sys.argv)
    window = CRMWindow()
    window.show()
    sys.exit(app.exec_())
