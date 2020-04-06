import unittest

from chapter_03.province import Province
from chapter_03.province_data import sample_province_data


class TestProvince(unittest.TestCase):
    def setUp(self) -> None:
        self.asia = Province(sample_province_data())

    def test_shortfall(self):
        self.assertEqual(self.asia.shortfall, 5)

    def test_profit(self):
        self.assertEqual(self.asia.profit, 230)

    def test_change_production(self):
        self.asia.produces[0].production = 20
        self.assertEqual(self.asia.shortfall, -6)
        self.assertEqual(self.asia.profit, 292)

    def test_zero_demand(self):
        self.asia.demand = 0
        self.assertEqual(self.asia.shortfall, -25)
        self.assertEqual(self.asia.profit, 0)

    def test_negative_demand(self):
        self.asia.demand = -1
        self.assertEqual(self.asia.shortfall, -26)
        self.assertEqual(self.asia.profit, -10)

    def test_empty_string_demand(self):
        self.asia.demand = ''
        self.assertEqual(self.asia.shortfall, -25)
        self.assertEqual(self.asia.profit, 0)


class TestNoProducers(unittest.TestCase):
    def setUp(self) -> None:
        data = {
            'name': 'No produces',
            'producers': [],
            'demand': 30,
            'price': 20
        }
        self.no_producers = Province(data)

    def test_shortfall(self):
        self.assertEqual(self.no_producers.shortfall, 30)

    def test_profit(self):
        self.assertEqual(self.no_producers.profit, 0)


class TestStringForProducers(unittest.TestCase):
    def setUp(self) -> None:
        data = {
            'name': 'string produces',
            'producers': '',
            'demand': 30,
            'price': 20
        }
        self.prov = Province(data)

    def test_shortfall(self):
        self.assertEqual(self.prov.shortfall, 30)


if __name__ == '__main__':
    unittest.main()
