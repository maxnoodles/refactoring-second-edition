# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2020-04-04
from chapter_01.create_statement_data import create_statement_data


def statement(invoice: dict, plays: dict):
    return render_plain_text(create_statement_data(invoice, plays))


def html_statement(invoice, plays):
    return render_html(create_statement_data(invoice, plays))


def render_html(data):
    result = f'<h1>Statement for ${data.customer}</h1>\n'
    result += "<table>\n"
    result += "<tr><th>play</th><th>seats</th><th>cost</th></tr>"
    for perf in data.performances:
        result += f'<tr><td>${perf.play.name}</td><td>${perf.audience}</td>'
        result += f'<td>${usd(perf.amount)}</td></tr>\n'

    result += "</table>\n"
    result += f'<p>Amount owed is <em>${usd(data.totalAmount)}</em></p>\n'
    result += f'<p>You earned <em>${data.totalVolumeCredits}</em> credits</p>\n'


def render_plain_text(data):
    result = f'Statement for {data["customer"]}\n'
    for perf in data['performances']:
        result += f'  {perf["play"]["name"]}: ${usd(perf["amount"])} ({perf["audience"]} seats)\n'

    result += f'Amount owed is {usd(data["total_amount"])}\n'
    result += f'You earned {data["total_volume_credits"]} credits\n'
    return result


def usd(a_number):
    return f'{a_number / 100:.2f}'
