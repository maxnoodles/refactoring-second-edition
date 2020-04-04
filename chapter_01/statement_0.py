# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2020-04-04
import json
from collections import namedtuple
from pathlib import Path


# def dict_to_object(obj_name, _dict):
#     return namedtuple(obj_name, _dict.keys())(*_dict.values())
#
#
# def json_fp_to_object(path):
#     obj_name = Path(path).name.split('.')[0]
#     print(obj_name)
#     with open(path, 'r', encoding='utf-8') as f:
#         obj_dict = json.load(f)
#         if isinstance(obj_dict, list):
#             obj_dict = obj_dict[0]
#         return dict_to_object(obj_name, obj_dict)
#
#
# invoice = json_fp_to_object('invoices.json')
# plays = json_fp_to_object('plays.json')
# print(str(invoice), str(plays))

def statement(invoice: dict, plays: dict):
    total_amount: int = 0
    volume_credits: int = 0
    result = f'Statement for {invoice["customer"]}\n'
    for perf in invoice['performances']:
        play = plays[perf['playID']]
        this_amount = 0
        play_type = play['type']
        if play_type == 'tragedy':
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)

        elif play_type == 'comedy':
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)
            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play_type}')

        #  add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if play_type == 'comedy':
            volume_credits += perf['audience'] // 5

        result += f'  {play["name"]}: ${this_amount / 100 :.2f} ({perf["audience"]} seats)\n'
        total_amount += this_amount
    result += f'Amount owed is {total_amount / 100 :.2f}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


def test_statement():
    with open('invoices.json', 'r', encoding='utf-8') as f:
        invoices = json.load(f)
        invoice = invoices[0]

    with open('plays.json', 'r', encoding='utf-8') as f:
        plays = json.load(f)

    print(statement(invoice, plays))


if __name__ == "__main__":
    test_statement()