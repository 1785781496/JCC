# -*- coding: utf-8 -*-
'''
1、WBS知道Task，包含task_id，一张表，快速查询到task
    模板，类型的问题都集中体现在这张表中
2、Task_detail一张表，
3、封装自己的API

'''


class SPGModel():
    def __init__(self, type=0):
        super(SPGModel, self).__init__()

    def show(self):
        print("Model")


if __name__ == '__main__':
    model = SPGModel()
    model.show()
