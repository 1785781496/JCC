# -*- coding: utf-8 -*-
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from data.customer import customer


class JCCTable(QWidget):
    def __init__(self, info_dict={}):
        super(JCCTable, self).__init__()
        self.info_dict = info_dict

        self.row_count = 8
        self.column_count = 10
        self.title_code_list = []
        self.title_name_list = []
        self.title_name_list = [u'代码', u'客户简称']

        self.build_ui()
        self.init_table()

    def build_ui(self):
        self.table_widget = QTableWidget()
        # self.table_widget.clear()
        self.table_widget.setRowCount(self.row_count)
        self.table_widget.setColumnCount(self.column_count)
        self.table_widget.setHorizontalHeaderLabels(self.title_name_list)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table_widget)
        self.setLayout(main_layout)

    def init_table(self):
        # self.table_widget.setIconSize(QSize(50, 80))
        print(self.info_dict)
        if self.info_dict:
            keys = self.info_dict.keys()
            print(keys)
            print(list(keys)[0])
            print(self.info_dict[list(keys)[0]])
            self.title_code_list = list(self.info_dict[list(keys)[0]].keys())
            print(self.title_code_list)
            target_image_hash_list = []
            for i in range(self.row_count):
                for code in self.title_code_list:
                    code_index = self.title_code_list.index(code)
                    self.table_widget.setRowHeight(i, 40)
                    item = QTableWidgetItem(self.info_dict[list(keys)[0]][code])
                    self.table_widget.setItem(i, code_index, item)


class JCCMain(QWidget):
    def __init__(self):
        super(JCCMain, self).__init__()
        self.setWindowTitle(u"杰瑞指挥中心")
        self.customer_dict = {}

        self.resize(1024, 512)
        self.load_customer_data()
        self.build_ui()

    def load_customer_data(self):
        self.customer_dict = customer.load_customer()

    def build_ui(self):
        tabwidget = QTabWidget()
        if self.customer_dict:
            customer_table = JCCTable(self.customer_dict)
            tabwidget.addTab(customer_table, u'客户')
        team_table = QWidget()
        task_table = QWidget()
        batch_req_table = QWidget()

        tabwidget.addTab(team_table, u'团队')
        tabwidget.addTab(task_table, u'任务')
        tabwidget.addTab(batch_req_table, u'批量需求')

        top_layout = QVBoxLayout()
        middle_layout = QVBoxLayout()
        middle_layout.addWidget(tabwidget)
        bottom_layout = QVBoxLayout()

        master_layout = QVBoxLayout()
        master_layout.addLayout(top_layout)
        master_layout.addLayout(middle_layout)
        master_layout.addLayout(bottom_layout)
        self.setLayout(master_layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JCCMain()
    window.show()
    sys.exit(app.exec_())


