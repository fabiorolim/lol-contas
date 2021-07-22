import unittest

from simulador_financeiro import Price, Sac


class TestPrice(unittest.TestCase):

    def setUp(self) -> None:
        self.price = Price(26000, 4, 3)

    def test_calc_pmt(self):
        self.assertEqual(self.price.pmt, 9369.06)

    def test_calc_interest_month_1(self):
        self.assertEqual(self.price._calc_interest(), 1040)

    def test_calc_amortization(self):
        self.assertEqual(self.price._calc_amortization(1040), 8329.06)

    def test_calc_out_balance(self):
        self.price._calc_out_balance(8329.06)
        self.assertEqual(self.price.pv, 17670.94)


class TestSac(unittest.TestCase):

    def setUp(self) -> None:
        self.sac = Sac(30000, 3, 10)

    def test_calc_pmt(self):
        self.assertEqual(self.sac.pmt, 3900)

    def test_calc_interest_month_1(self):
        self.assertEqual(self.sac._calc_interest(), 900)

    def test_calc_amortization(self):
        self.assertEqual(self.sac.a, 3000)

    def test_calc_out_balance(self):
        self.sac._calc_out_balance()
        self.assertEqual(self.sac.pv, 27000)
