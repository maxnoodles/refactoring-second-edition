import json
import unittest

from chapter_01 import statement_0
from chapter_01 import statement_1
from chapter_01.create_statement_data import create_statement_data


class TestStatement(unittest.TestCase):

    def setUp(self) -> None:
        with open('../../chapter_01/invoices.json', 'r', encoding='utf-8') as f:
            invoices = json.load(f)
            self.invoice = invoices[0]

        with open('../../chapter_01/plays.json', 'r', encoding='utf-8') as f:
            self.plays = json.load(f)

            self.expect_statement_result = '''Statement for BigCo
  Hamlet: $650.00 (55 seats)
  As You Like It: $580.00 (35 seats)
  Othello: $500.00 (40 seats)
Amount owed is 1730.00
You earned 47 credits
'''

    def test_statement_0(self):

        result = statement_0.statement(self.invoice, self.plays)
        self.assertEqual(result, self.expect_statement_result)

    def test_statement_1(self):

        result = statement_1.statement(self.invoice, self.plays)

        self.assertEqual(result, self.expect_statement_result)

    def test_create_statement_data(self):
        result = create_statement_data(self.invoice, self.plays)
        # print(result)
        expect_statement_data = {'customer': 'BigCo', 'performances': [{'playID': 'hamlet', 'audience': 55, 'play': {'name': 'Hamlet', 'type': 'tragedy'}, 'amount': 65000, 'volume_credits': 25}, {'playID': 'as-like', 'audience': 35, 'play': {'name': 'As You Like It', 'type': 'comedy'}, 'amount': 58000, 'volume_credits': 12}, {'playID': 'othello', 'audience': 40, 'play': {'name': 'Othello', 'type': 'tragedy'}, 'amount': 50000, 'volume_credits': 10}], 'total_volume_credits': 47, 'total_amount': 173000}
        self.assertEqual(result, expect_statement_data)


if __name__ == '__main__':
    unittest.main()
