# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2020-04-09
from copy import deepcopy

organization = {'name': "Acme Gooseberries", 'country': "GB"}
result = ''
result += f"<h1>{organization['name']}</h1>"
organization['name'] = 'new_name'


class Organization:

    def __init__(self, data):
        self._name = data['name']
        self._country = data['country']

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, a_string):
        self._name = a_string

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, a_country_code):
        self._country = a_country_code


organization = Organization({'name': "Acme Gooseberries", 'country': "GB"})


def get_organization():
    return organization


get_organization().name = 'new_name'
result += f"<h1>{get_organization().name}</h1>"

#############################################

customer_data_source = {
    '1920': {
        'name': "martin",
        'id': "1920",
        'usages': {
            "2016": {
                "1": 50,
                "2": 55,
            },
            "2015": {
                "1": 70,
                "2": 63,
            }
        }
    }
}
customer_id = '1920'
amount = 10
year = 2016
month = 1
customer_data_source[customer_id]['usages'][year][month] = amount


def compare_usage_source(customer_id, later_year, month):
    later = customer_data_source[customer_id]['usages'][later_year][month]
    earlier = customer_data_source[customer_id]['usages'][later_year - 1][month]
    return {'later_amount': later, 'change': later - earlier}


def get_raw_data_of_customers_source():
    return customer_data_source


def set_raw_data_of_customers_source(arg):
    customer_data = arg


get_raw_data_of_customers_source()[customer_id]['usages'][year][month] = amount


class CustomerData:
    def __init__(self, data):
        self._data = data

    def set_usage(self, customer_id, year, month, amount):
        self._data[customer_id]['usages'][year][month] = amount

    @property
    def raw_data(self):
        return deepcopy(self._data)

    def usage(self, customer_id, year, month):
        return self._data[customer_id]['usages'][year][month]


customer_data = CustomerData(customer_data_source)


def get_customer_data():
    return customer_data


def get_raw_data_of_customers():
    return customer_data.raw_data


def set_raw_data_of_customers(arg):
    customer_data = CustomerData(arg)


get_customer_data().set_usage(customer_id, year, month, amount)


def compare_usage(customer_id, later_year, month):
    later = get_customer_data().usage(customer_id, later_year, month)
    earlier = get_customer_data().usage(customer_id, later_year - 1, month)
    return {'later_amount': later, 'change': later - earlier}
