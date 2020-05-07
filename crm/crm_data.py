# -*- coding: utf-8 -*-
from data.customer.customer import Customer


def init_customer_info():
    customer_info_dict = {}

    def add_customer(obj):
        if obj.get_code() not in customer_info_dict.keys():
            customer_info_dict[obj.get_code()] = obj.get_name()

    customer = Customer('yh', u'艺画开天')
    add_customer(customer)
    print(customer_info_dict)


def get_customer_list():
    return [u'童话', u'灏日', u'良子', u'凝羽', u'声画']


def get_info_list():
    return [u'基本信息', u'合同信息', u'问题列表', u'开发列表', u'更新列表']


if __name__ == '__main__':
    # init_customer_info()
    get_customer_list()

