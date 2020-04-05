# -*- coding:utf-8 -*-
#
#
# Author: noodles
# Date: 2020-04-05


class Producer:
    def __init__(self, a_province, data):
        self._province = a_province
        self._cost = data['cost']
        self._name = data['name']
        self._production = data['production'] or 0

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, arg):
        self._cost = int(arg)

    @property
    def production(self):
        return self._production

    @production.setter
    def production(self, amount_str):
        new_production = int(amount_str) if amount_str else 0
        self._province.total_production += new_production - self._production
        self._production = new_production