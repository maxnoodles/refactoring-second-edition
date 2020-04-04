import json
import unittest

from chapter_01 import statement_0
from chapter_01 import statement_1


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        with open('invoices.json', 'r', encoding='utf-8') as f:
            invoices = json.load(f)
            self.invoice = invoices[0]

        with open('plays.json', 'r', encoding='utf-8') as f:
            self.plays = json.load(f)

            self.expect_result = '''Statement for BigCo
  Hamlet: $650.00 (55 seats)
  As You Like It: $580.00 (35 seats)
  Othello: $500.00 (40 seats)
Amount owed is 1730.00
You earned 47 credits
'''

    def test_statement_0(self):

        result = statement_0.statement(self.invoice, self.plays)
        self.assertEqual(result, self.expect_result)

    def test_statement_1(self):

        result = statement_1.statement(self.invoice, self.plays)

        self.assertEqual(result, self.expect_result)


if __name__ == '__main__':
    unittest.main()
