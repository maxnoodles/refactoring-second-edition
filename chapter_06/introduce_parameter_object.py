# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2020-04-08


def amount_invoiced_source(start_data, end_data):
    pass


def amount_invoiced(a_data_range):
    pass


station = {
    'name': 'ZB1',
    'readings': [
        {'temp': 47, 'time': "2016-11-10 09:10"},
        {'temp': 53, 'time': "2016-11-10 09:20"},
        {'temp': 58, 'time': "2016-11-10 09:30"},
        {'temp': 53, 'time': "2016-11-10 09:40"},
        {'temp': 51, 'time': "2016-11-10 09:50"},
    ]
}

operating_plan = {
    'temperatureFloor': 35,
    'temperatureCeiling': 39
}


def reading_outside_range_source(station, min_, max_):
    return filter(lambda x: x < min_ or x > max_, station['readings'])


alerts_source = reading_outside_range_source(station,
                               operating_plan['temperatureFloor'],
                               operating_plan['temperatureCeiling'])


class NumberRange:

    def __init__(self, min_, max_):
        self._data = {
            'min': min_,
            'max': max_
        }

    @property
    def min_(self):
        return self._data['min']

    @property
    def max_(self):
        return self._data['max']

    def contains(self, arg):
        return self.min_ < arg < self.max_


temperature_range = NumberRange(operating_plan['temperatureFloor'],
                                operating_plan['temperatureCeiling'])


def reading_outside_range(station, temperature_range: NumberRange):
    return filter(lambda x: not temperature_range.contains(x), station['readings'])


alerts = reading_outside_range(station, temperature_range)
