from unittest.mock import MagicMock

from sample_5_mocks.owner import Owner


class TestOwner:
    FIRST_NAME = 'test_name'
    LAST_NAME = 'test_surname'

    def setup_method(self) -> None:
        self.wallet_mock = MagicMock()  # == Wallet()
        self.owner = Owner(self.FIRST_NAME, self.LAST_NAME, self.wallet_mock)

    def test_owner_first_name(self):
        result = self.owner.first_name
        assert result == self.FIRST_NAME

    def test_owner_last_name(self):
        assert self.owner.last_name == self.LAST_NAME

    def test_owner_supply_to_wallet(self):
        cash_to_supply = 10
        self.owner.supply_wallet(cash_to_supply)
        self.wallet_mock.add_cash.assert_called_once_with(cash_to_supply)

    def test_owner_withdraw_money(self):
        cash_to_withdraw = 10
        self.owner.withdraw_money(cash_to_withdraw)
        self.wallet_mock.spend_cash.assert_called_once_with(cash_to_withdraw)

    def test_owner_check_if_can_afford_true(self):
        cash_to_validate = 10
        mocked_balance_value = 10
        self.wallet_mock.get_balance.return_value = mocked_balance_value

        can_afford_result = self.owner.check_if_can_afford(cash_to_validate)

        assert can_afford_result is True
        self.wallet_mock.get_balance.assert_called_once()





