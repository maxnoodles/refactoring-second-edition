# -*- coding:utf-8 -*-
#
# Author: noodles
# Date: 2020-04-07
from copy import deepcopy

default_owner_data = {'first_name': "Martin", 'last_name': "Fowler"}


def get_default_owner():
    # return deepcopy(default_owner_data)
    return Person(default_owner_data)


def set_default_owner(arg):
    default_owner_data = arg


class Person:

    def __init__(self, data):
        self._last_name = data['last_name']
        self._first_name = data['first_name']


spaceship = dict()
spaceship['owner'] = default_owner_data


default_owner = {'firstName': "Rebecca", 'lastName': "Parsons"}

spaceship['owner'] = get_default_owner()
set_default_owner({'firstName': "Rebecca", 'lastName': "Parsons"})

