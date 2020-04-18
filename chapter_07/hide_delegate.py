# -*- coding:utf-8 -*-
#
# Author: noodles
# Date: 2020-04-12


class Person:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, arg):
        self._department = arg

    @property
    def manager(self):
        return self._department.manager

    @manager.setter
    def manager(self, arg):
        self._manager = arg


class Department:

    @property
    def charge_code(self):
        return self._charge_code

    @charge_code.setter
    def charge_code(self, arg):
        self._charge_code = arg

    @property
    def manager(self):
        return self._manager

    @manager.setter
    def manager(self, arg):
        self._manager = arg


a_person = Person('test')
# manager = a_person.department.manager
manager = a_person.manager