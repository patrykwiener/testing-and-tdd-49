import unittest

from parameterized import parameterized

from sample_5_mocks.wallet import Wallet, InsufficientAmount


class TestWallet(unittest.TestCase):
    TEST_TRANSACTIONS_PARAMS = [
        (30, 10, 20),
        (20, 20, 0),
    ]

    def setUp(self) -> None:
        self.empty_wallet = Wallet()
        self.wallet = Wallet(20)

    def test_default_initial_amount(self):
        self.assertEqual(self.empty_wallet.get_balance(), 0, 'Wallet initial amount does not equal 0')

    def test_setting_initial_amount(self):
        self.assertEqual(self.wallet.get_balance(), 20, 'Wallet initial amount does not equal 20')

    def test_spend_cash(self):
        self.wallet.spend_cash(10)
        self.assertEqual(self.wallet.get_balance(), 10,
                         'In Wallet with balance 20 amount after spending 10 does not equal 10')

    def test_add_cash(self):
        self.wallet.add_cash(80)
        self.assertEqual(self.wallet.get_balance(), 100,
                         'In Wallet with balance 20 amount after adding 80 does not equal 100')

    def test_spend_cash_raises_exception_on_insufficient_amount(self):
        with self.assertRaises(InsufficientAmount, msg='Not raised on spending more money than available'):
            self.empty_wallet.spend_cash(10)

    @parameterized.expand([
        (30, 10, 20),
        (20, 20, 0),
    ])
    def test_transactions(self, earned, spending, expected):
        self.empty_wallet.add_cash(earned)
        self.empty_wallet.spend_cash(spending)
        self.assertEqual(self.empty_wallet.get_balance(), expected, 'Balance does not equal the expected')

    def test_transactions_with_subTest(self):
        for earned, spending, expected in self.TEST_TRANSACTIONS_PARAMS:
            with self.subTest():
                self.setUp()  # wymagana ponowna inicjalizacja obiektów!!!
                self.empty_wallet.add_cash(earned)
                self.empty_wallet.spend_cash(spending)
                self.assertEqual(self.empty_wallet.get_balance(), expected, 'Balance does not equal the expected')
