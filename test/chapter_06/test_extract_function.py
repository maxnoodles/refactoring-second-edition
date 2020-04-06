import unittest

from chapter_06.extract_function import print_owing_source, print_owing
from chapter_06.invoice_data import sample_invoice_date


class TestExtractFunction(unittest.TestCase):
    def setUp(self) -> None:
        self.invoice = sample_invoice_date()
        self.expect_result_invoice = {
            'customer': 'BigCo',
            'orders': [
                {'playID': 'hamlet', 'audience': 55,
                 'play': {'name': 'Hamlet', 'type': 'tragedy'}, 'amount': 65000,
                 'volume_credits': 25},
                {'playID': 'as-like', 'audience': 35,
                 'play': {'name': 'As You Like It', 'type': 'comedy'}, 'amount': 58000,
                 'volume_credits': 12},
                {'playID': 'othello', 'audience': 40,
                 'play': {'name': 'Othello', 'type': 'tragedy'}, 'amount': 50000,
                 'volume_credits': 10}], 'total_volume_credits': 47, 'total_amount': 173000,
            'dueDate': '2020/05/06'
        }

    def test_print_owing_source(self):
        result = print_owing_source(self.invoice)
        self.assertEqual(result, self.expect_result_invoice)

    def test_print_owing(self):
        result = print_owing(self.invoice)
        self.assertEqual(result, self.expect_result_invoice)


if __name__ == '__main__':
    unittest.main()
