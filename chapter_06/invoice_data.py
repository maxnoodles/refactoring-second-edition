# -*- coding:utf-8 -*-
#
# Author: noodles
# Date: 2020-04-06


def sample_invoice_date():
    return {
        'customer': 'BigCo',
        'orders': [

            {
                'playID': 'hamlet',
                'audience': 55,
                'play': {
                    'name': 'Hamlet',
                    'type': 'tragedy'
                },
                'amount': 65000,
                'volume_credits': 25
            },
            {
                'playID': 'as-like',
                'audience': 35,
                'play': {
                    'name': 'As You Like It',
                    'type': 'comedy'
                },
                'amount': 58000,
                'volume_credits': 12
            },
            {
                'playID': 'othello',
                'audience': 40,
                'play': {
                    'name': 'Othello',
                    'type': 'tragedy'
                },
                'amount': 50000,
                'volume_credits': 10
            }
        ],
        'total_volume_credits': 47,
        'total_amount': 173000
    }

