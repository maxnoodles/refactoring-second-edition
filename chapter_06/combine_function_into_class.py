# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2020-04-08
from copy import deepcopy

reading = {'customer': "ivan", 'quantity': 10, 'month': 5, 'year': 2017}


def acquire_reading():
    return reading


def base_rage(month, year):
    return int()


def tax_threshold(year):
    return int()


def calculate_base_charge(a_reading):
    return base_rage(a_reading['month'], a_reading['year']) * a_reading['quantity']


def customer_1():
    a_reading = acquire_reading()
    base_charge = base_rage(a_reading['month'], a_reading['year']) * a_reading['quantity']
    return base_charge


def customer_2_source():
    a_reading = acquire_reading()
    base = base_rage(a_reading['month'], a_reading['year']) * a_reading['quantity']
    taxable_charge = max(0, base - tax_threshold(a_reading['year']))
    return taxable_charge


def customer_3_source():
    a_reading = acquire_reading()
    basic_charge_amount = calculate_base_charge(a_reading)
    return basic_charge_amount


def enrich_reading(original):
    # 测试原始数据不会被修改
    result = deepcopy(original)
    result['base_charge'] = calculate_base_charge(result)
    result['taxable_charge'] = max(0, result['base_charge'] - tax_threshold(result['year']))
    return result


def customer_3():
    raw_reading = acquire_reading()
    a_reading = enrich_reading(raw_reading)
    basic_charge_amount = a_reading['base_charge']
    return basic_charge_amount


def customer_2():
    raw_reading = acquire_reading()
    a_reading = enrich_reading(raw_reading)
    taxable_charge = a_reading['taxable_charge']
    return taxable_charge
