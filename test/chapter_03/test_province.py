import unittest

from chatper_03.province import Province
from chatper_03.province_data import sample_province_data


class TestProvince(unittest.TestCase):
    def setUp(self) -> None:
        self.asia = Province(sample_province_data())

    def test_shortfall(self):
        self.assertEqual(self.asia.shortfall, 5)


if __name__ == '__main__':
    unittest.main()
