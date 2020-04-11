# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2020-04-10


class Priority:

    def __init__(self, value):
        if value not in self.legal_value():
            raise ValueError(f'{value} is invalid for Priority')
        self._value = value

    @property
    def _index(self):
        return self.legal_value().index(self._value)

    @staticmethod
    def legal_value():
        return ['low', 'normal', 'high', 'rush']

    def __eq__(self, other):
        return self._index == other._index

    def __gt__(self, other):
        return self._index > other._index

    def __lt__(self, other):
        return self._index < other._index

    def __repr__(self):
        return self._value


class Order:

    def __init__(self, data):
        self._priority = data['priority']

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, a_string):
        self._priority = Priority(a_string)

    @property
    def priority_string(self):
        return str(self._priority)


order = {
    'priority': 'rush'
}
order = Order(order)
order.priority = 'high'

orders = [order]

high_priority_count = len(list(filter(lambda x: x.priority_string in ['high', 'rush'], orders)))
high_priority_count2 = len(list(filter(lambda x: x.priority > Priority('normal'), orders)))
# TODO 编写测试替换打印语句
print(high_priority_count, high_priority_count2)
