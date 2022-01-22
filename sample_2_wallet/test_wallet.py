import pytest

from sample_2_wallet.wallet import Wallet, InsufficientAmount


def generate():
    array = []
    for _ in range(10):
        array.append([10, 10, 0])
    return array

PARAMETRIZED_ARRAY = generate()

class TestWallet:
    amount = 100

    def setup_method(self):
        self.empty_wallet = Wallet()
        self.wallet = Wallet(amount=self.amount)

    def test_default_initial_amount(self):
        expected = 0

        result = self.empty_wallet.get_balance()

        assert result == expected
        # assert Wallet().get_balance() == 0

    def test_setting_initial_amount(self):
        result = self.wallet.get_balance()

        assert result == self.amount

    def test_spend_cash(self):
        spending = 40
        expected = 60

        self.wallet.spend_cash(spending=spending)
        result = self.wallet.get_balance()

        assert result == expected

    def test_add_cash(self):
        cash = 40
        expected = 140

        self.wallet.add_cash(cash=cash)
        result = self.wallet.get_balance()

        assert result == expected

    def test_spend_cash_raises_exception_on_insufficient_amount(self):
        spending = 10

        with pytest.raises(InsufficientAmount):
            self.empty_wallet.spend_cash(spending=spending)

    # @pytest.mark.parametrize('cash,spending,expected', PARAMETRIZED_ARRAY)
    @pytest.mark.parametrize('cash,spending,expected', [
        [30, 20, 10],
        [20, 20, 0],
    ])
    def test_transaction_success(self, cash, spending, expected):
        self.empty_wallet.add_cash(cash=cash)
        self.empty_wallet.spend_cash(spending=spending)

        result = self.empty_wallet.get_balance()

        assert result == expected
