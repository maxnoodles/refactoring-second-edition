# -*- coding:utf-8 -*-
#
# Author: noodles
# Date: 2020-04-06


def get_base_price_source(an_order):
    base_price = an_order['base_price']
    return base_price > 1000


def get_base_price(an_oder):
    return an_oder['base_price'] > 1000
