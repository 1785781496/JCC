# -*- coding: utf-8 -*-

from api.json_api import *

class Customer():
    def __init__(self):
        self.name = ""
        self.customer_code = ""


def get_json():
    json_api = JsonAPI("customer")
    json_api.set_json_file_path(os.path.dirname(__file__))
    return json_api


def load_customer():
    return get_json().read_json_from_file()


def save_customer(c_dict):
    get_json().write_json_to_file(c_dict)


def load(type):
    if type == 'json':
        pass
    elif type == 'excel':
        pass
    else:
        pass


if __name__ == '__main__':
    customer_dict = {}
    info_dict = {'code': u'hr', 'brief_name': u"灏日影视"}

    customer_dict['hr'] = info_dict
    save_customer(customer_dict)
    print(load_customer())
