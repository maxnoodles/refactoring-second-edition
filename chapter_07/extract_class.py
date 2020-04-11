# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2020-04-11


class PersonSource:

    def __init__(self, data):
        self._name = data['name']
        self._office_area_code = data['office_area_code']
        self._office_number = data['office_number']

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, arg):
        self._name = arg

    @property
    def office_area_code(self):
        return self._office_area_code

    @office_area_code.setter
    def office_area_code(self, arg):
        self._office_area_code = arg

    @property
    def office_number(self):
        return self._office_number

    @office_number.setter
    def office_number(self, arg):
        self._office_number = arg


class Person:

    def __init__(self, data):
        self._name = data['name']
        self._telephone_number = TelephoneNumber(data['office_area_code'], data['office_number'])

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, arg):
        self._name = arg

    @property
    def office_area_code(self):
        return self._telephone_number._area_code

    @office_area_code.setter
    def office_area_code(self, arg):
        self._telephone_number._area_code = arg

    @property
    def office_number(self):
        return self._telephone_number.number

    @office_number.setter
    def office_number(self, arg):
        self._telephone_number.number = arg

    @property
    def telephone_number(self):
        return str(self._telephone_number)


class TelephoneNumber:
    def __init__(self, area_code, number):
        self._area_code = area_code
        self.number = number

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, arg):
        self._area_code = arg

    @property
    def number(self):
        return self.number

    @number.setter
    def number(self, arg):
        self.number = arg

    @property
    def __repr__(self):
        return f'{self._area_code} {self.number}'

