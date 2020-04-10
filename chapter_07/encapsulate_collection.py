# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2020-04-10


class PersonSource:

    def __init__(self, name):
        self._name = name
        self._courses = []

    @property
    def name(self):
        return self._name

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, a_list):
        self._courses = a_list


class CourseSource:

    def __init__(self, name, is_advanced):
        self._name = name
        self._is_advanced = is_advanced

    @property
    def name(self):
        return self._name

    @property
    def is_advanced(self):
        return self._is_advanced


a_person = PersonSource('noodles')
num_advanced = filter(lambda x: x.is_advanced, a_person.courses)


def append_course_source(name, false):
    a_person.courses.append(CourseSource(name, false))


class Person:

    def __init__(self, name):
        self._name = name
        self._courses = []

    @property
    def name(self):
        return self._name

    @property
    def courses(self):
        return self._courses[:]

    @courses.setter
    def courses(self, a_list):
        self._courses = a_list[:]

    def add_course(self, a_course):
        return self._courses.append(a_course)

    def remove_course(self, a_course):
        if a_course not in self._courses:
            raise ValueError(f'{a_course.name} is not in course_list')
        else:
            self._courses.remove(a_course)


a_person = Person('noodles')

def append_course(name, false):
    a_person.add_course(CourseSource(name, false))