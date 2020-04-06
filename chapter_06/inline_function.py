# -*- coding:utf-8 -*-
#
# Author: noodles
# Date: 2020-04-06


def get_rating_source(driver):
    return 2 if more_than_five_late_deliveries(driver) else 1


def get_rating(a_driver):
    return 2 if a_driver.number_of_late_deliveries > 5 else 1


def report_lines_source(a_customer):
    lines = []
    gather_customer_date(lines, a_customer)
    return lines


def report_lines(a_customer):
    lines = []
    lines.append(['name', a_customer['name']])
    lines.append(['location', a_customer['location']])
    return lines


def gather_customer_date(lines, a_customer):
    lines.append(['name', a_customer['name']])
    lines.append(['location', a_customer['location']])


def more_than_five_late_deliveries(driver):
    return driver.number_of_late_deliveries > 5


