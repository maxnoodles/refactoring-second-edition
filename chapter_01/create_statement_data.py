# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2020-04-04


def create_statement_data(invoice, plays):
    def volume_credits_for(perf):
        result: int = 0
        result += max(perf['audience'] - 30, 0)
        if perf["play"]['type'] == 'comedy':
            result += perf['audience'] // 5
        return result

    def amount_for(a_performance):
        result: int = 0
        play_type = a_performance["play"]['type']
        if play_type == 'tragedy':
            result = 40000
            if a_performance['audience'] > 30:
                result += 1000 * (a_performance['audience'] - 30)

        elif play_type == 'comedy':
            result = 30000
            if a_performance['audience'] > 20:
                result += 10000 + 500 * (a_performance['audience'] - 20)
            result += 300 * a_performance['audience']

        else:
            raise ValueError(f'unknown type: {play_type}')
        return result

    def total_volume_credits(data):
        return sum([perf['volume_credits'] for perf in data['performances']])

    def total_amount(data):
        return sum([perf['amount'] for perf in data['performances']], 0)

    def enrich_performance(a_performance):
        def play_for(a_performance):
            return plays[a_performance['playID']]

        result = dict(a_performance)
        result['play'] = play_for(result)
        result['amount'] = amount_for(result)
        result['volume_credits'] = volume_credits_for(result)
        return result

    statement_data = dict()
    statement_data['customer'] = invoice['customer']
    statement_data['performances'] = list(map(enrich_performance, invoice['performances']))
    statement_data['total_volume_credits'] = total_volume_credits(statement_data)
    statement_data['total_amount'] = total_amount(statement_data)
    return statement_data