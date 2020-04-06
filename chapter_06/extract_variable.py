# -*- coding:utf-8 -*-
#
# Author: noodles
# Date: 2020-04-06


class OrderSource:

    def __init__(self, a_record):
        self._data = a_record

    @property
    def quantity(self):
        return self._data['quantity']

    @property
    def item_price(self):
        return self._data['item_price']

    @property
    def price(self):
        return self.quantity * self.item_price - \
               max(0, self.quantity - 500) * self.item_price * 0.05 + \
               min(self.quantity * self.item_price * 0.1, 100)


class Order:

    def __init__(self, a_record):
        self._data = a_record

    @property
    def quantity(self):
        return self._data['quantity']

    @property
    def item_price(self):
        return self._data['item_price']

    @property
    def price(self):
        return self.base_price - self.quantity_discount + self.shipping

    @property
    def base_price(self):
        return self.quantity * self.item_price

    @property
    def quantity_discount(self):
        return max(0, self.quantity - 500) * self.item_price * 0.05

    @property
    def shipping(self):
        return min(self.quantity * self.item_price * 0.1, 100)
