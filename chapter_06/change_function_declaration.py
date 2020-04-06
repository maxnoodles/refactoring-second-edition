# -*- coding:utf-8 -*-
#
# Author: noodles
# Date: 2020-04-06
import math


def use_circumference():
    # circum_source(5)
    # circum(5)
    return circumference(5)


def circum_source(radius):
    return 2 * math.pi * radius


def circum(radius):
    return circumference(radius)


def circumference(radius):
    return 2 * math.pi * radius


class BookSource:

    def __init__(self):
        self._reservations = []

    def add_reservation(self, customer):
        self._reservations.append(customer)


class Book:

    def __init__(self):
        self._reservations = []

    def add_reservation(self, customer):
        self.zz_add_reservation(customer, False)

    def zz_add_reservation(self, customer, is_priority):
        assert isinstance(is_priority, bool)
        self._reservations.append(customer)


def new_englanders_source(some_customer: list):
    return filter(in_new_england_source, some_customer)


def in_new_england_source(a_customer):
    return a_customer['address']['state'] in ["MA", "CT", "ME", "VT", "NH", "RI"]


def new_englanders(some_customer: list):
    return filter(xx_new_in_new_england, [c['address']['state'] for c in some_customer])


def in_new_england(a_customer):
    state_code = a_customer['address']['state']
    return xx_new_in_new_england(state_code)


def xx_new_in_new_england(state_code):
    return state_code in ["MA", "CT", "ME", "VT", "NH", "RI"]

