import sys

from PySide2.QtWidgets import *


class ConfigStep(QWidget):
    def __init__(self):
        super(ConfigStep, self).__init__()
        self.config_step_list = [u'Project_root', u'Project']
        self.build_ui()

    def build_ui(self):
        self.main_layout = QGridLayout()

        self.checkbox_project_root = QCheckBox("Project Root : ")
        self.line_edit_project_root = QLineEdit("D:/projects")

        self.main_layout.addWidget(self.checkbox_project_root, 0, 0, 1, 1)
        self.main_layout.addWidget(self.line_edit_project_root, 0, 1, 1, 5)

        self.checkbox_project = QCheckBox("Project : ")
        self.line_edit_project = QLineEdit("zzz")

        self.main_layout.addWidget(self.checkbox_project, 1, 0, 1, 1)
        self.main_layout.addWidget(self.line_edit_project, 1, 1, 1, 5)

        self.checkbox_asset_type = QCheckBox("Asset Type : ")
        self.line_edit_asset_type = QLineEdit("Char")

        self.main_layout.addWidget(self.checkbox_asset_type, 2, 0, 1, 1)
        self.main_layout.addWidget(self.line_edit_asset_type, 2, 1, 1, 5)

        self.checkbox_asset = QCheckBox("Asset : ")
        self.line_edit_asset = QLineEdit("C001")

        self.main_layout.addWidget(self.checkbox_asset, 3, 0, 1, 1)
        self.main_layout.addWidget(self.line_edit_asset, 3, 1, 1, 5)

        self.checkbox_asset_step = QCheckBox("Asset Step: ")
        self.line_edit_asset_step = QLineEdit("Model")

        self.main_layout.addWidget(self.checkbox_asset_step, 4, 0, 1, 1)
        self.main_layout.addWidget(self.line_edit_asset_step, 4, 1, 1, 5)

        self.btn_confirm = QPushButton(u"确定")
        self.btn_confirm.clicked.connect(self.step_confirm)
        self.main_layout.addWidget(self.btn_confirm, 5, 1, 1, 5)

        self.setLayout(self.main_layout)

    def step_confirm(self):
        print("Confirm")
        msg = "{}/{}/{}/{}/{}".format(self.line_edit_project_root.text(),
                                      self.line_edit_project.text(),
                                      self.line_edit_asset_type.text(),
                                      self.line_edit_asset.text(),
                                      self.line_edit_asset_step.text())
        print(msg)


class ConfigTree(QTreeWidget):
    def __init__(self):
        super(ConfigTree, self).__init__()
        self.build_ui()

    def build_ui(self):
        self.main_layout = QHBoxLayout()


class SPGMain(QWidget):
    def __init__(self):
        super(SPGMain, self).__init__()
        self.setWindowTitle(u"Spider配置导引")
        self.config_step_list = []
        self.build_ui()

    def build_ui(self):
        self.top_layout = QHBoxLayout()
        self.label = QLabel(u"Spider配置步骤")
        self.top_layout.addWidget(self.label)

        self.mid_layout = QHBoxLayout()

        self.mid_left_layout = QHBoxLayout()
        self.config_widget = ConfigStep()
        self.mid_left_layout.addWidget(self.config_widget)

        self.mid_right_layout = QHBoxLayout()
        self.tree_widget = ConfigTree()
        self.mid_right_layout.addWidget(self.tree_widget)

        self.mid_layout.addLayout(self.mid_left_layout, 1)
        self.mid_layout.addLayout(self.mid_right_layout, 1)

        self.master_layout = QVBoxLayout()
        self.master_layout.addLayout(self.top_layout)
        self.master_layout.addLayout(self.mid_layout)

        self.resize(800, 600)
        self.setLayout(self.master_layout)


if __name__ == '__main__':
    print("SPG Begins.")
    app = QApplication(sys.argv)
    window = SPGMain()
    window.show()
    sys.exit(app.exec_())
