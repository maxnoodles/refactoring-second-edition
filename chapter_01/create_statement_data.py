# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2020-04-04


def create_statement_data(invoice: dict, plays: dict) -> dict:
    # def volume_credits_for(a_performance):
    #     return PerformanceCalculator(a_performance, play_for(a_performance)).volume_credits

    # def amount_for(a_performance):
    #     return PerformanceCalculator(a_performance, play_for(a_performance)).amount

    def total_volume_credits(data):
        return sum([perf['volume_credits'] for perf in data['performances']])

    def total_amount(data):
        return sum([perf['amount'] for perf in data['performances']], 0)

    def play_for(a_performance):
        return plays[a_performance['playID']]

    def enrich_performance(a_performance):
        calculator = create_performance_calculator(a_performance, play_for(a_performance))
        result = dict(a_performance)
        result['play'] = calculator.play
        result['amount'] = calculator.amount
        result['volume_credits'] = calculator.volume_credits
        return result

    statement_data = dict()
    statement_data['customer'] = invoice['customer']
    statement_data['performances'] = list(map(enrich_performance, invoice['performances']))
    statement_data['total_volume_credits'] = total_volume_credits(statement_data)
    statement_data['total_amount'] = total_amount(statement_data)
    return statement_data


def create_performance_calculator(a_performance, a_play):
    return PerformanceCalculator(a_performance, a_play)


class PerformanceCalculator:

    def __init__(self, a_performance, a_play):
        self.performance = a_performance
        self.play = a_play

    @property
    def amount(self):
        result = 0
        if self.play['type'] == 'tragedy':
            result = 40000
            if self.performance['audience'] > 30:
                result += 1000 * (self.performance['audience'] - 30)

        elif self.play['type'] == 'comedy':
            result = 30000
            if self.performance['audience'] > 20:
                result += 10000 + 500 * (self.performance['audience'] - 20)
            result += 300 * self.performance['audience']

        else:
            raise ValueError(f'unknown type: {self.play["type"]}')
        return result

    @property
    def volume_credits(self):
        result = 0
        result += max(self.performance['audience'] - 30, 0)
        if self.play['type'] == 'comedy':
            result += self.performance['audience'] // 5
        return result
