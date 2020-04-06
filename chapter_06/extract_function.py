# -*- coding:utf-8 -*-
#
# Author: noodles
# Date: 2020-04-06
import datetime


def print_owing_source(invoice: dict):
    outstanding = 0

    print("***********************")
    print("**** Customer Owes ****")
    print("***********************")

    for order in invoice['orders']:
        outstanding += order['amount']

    # record due data
    today = datetime.datetime.today()
    invoice['dueDate'] = (today + datetime.timedelta(days=30)).strftime("%Y/%m/%d")

    # print detail
    print(f'name: {invoice["customer"]}')
    print(f'amount: {outstanding}')
    print(f'due: {invoice["dueDate"]}')
    return invoice


def print_owing(invoice):
    print_banner()
    outstanding = calculate_outstanding(invoice)
    record_due_date(invoice)
    print_details(invoice, outstanding)
    return invoice


def calculate_outstanding(invoice):
    result = 0
    for order in invoice['orders']:
        result += order['amount']
    return result


def print_details(invoice, outstanding):
    print(f'name: {invoice["customer"]}')
    print(f'amount: {outstanding}')
    print(f'due: {invoice["dueDate"]}')


def print_banner():
    print("***********************")
    print("**** Customer Owes ****")
    print("***********************")


def record_due_date(invoice):
    today = datetime.datetime.today()
    invoice['dueDate'] = (today + datetime.timedelta(days=30)).strftime("%Y/%m/%d")


