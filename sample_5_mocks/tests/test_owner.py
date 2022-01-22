from unittest.mock import Mock

from sample_5_mocks.owner import Owner


class TestOwner:
    FIRST_NAME = 'test_name'
    LAST_NAME = 'test_surname'

    def setup_method(self):
        self.wallet_mock = Mock()  # == Wallet()
        self.owner = Owner(
            first_name=self.FIRST_NAME,
            last_name=self.LAST_NAME,
            wallet=self.wallet_mock,
        )

    def test_owner_first_name(self):
        result = self.owner.first_name
        assert result == self.FIRST_NAME

    def test_owner_last_name(self):
        assert self.owner.last_name == self.LAST_NAME

    def test_owner_supply_to_wallet(self):
        cash_to_supply = 10

        # wykonanie supply wallet
        self.owner.supply_wallet(cash=cash_to_supply)

        # assercja czy mock zostal wykonany
        self.wallet_mock.add_cash.assert_called_once_with(cash=cash_to_supply)

    def test_owner_withdraw_money(self):
        cash_to_withdraw = 10

        # wykonanie withdraw_money
        self.owner.withdraw_money(amount=cash_to_withdraw)

        # assercja czy mock zostal wykonany
        self.wallet_mock.spend_cash.assert_called_once_with(spending=cash_to_withdraw)

    def test_owner_check_if_can_afford_true(self):
        cash_to_validate = 20
        mocked_balance_value = 10
        # zamokowanie get_balance zeby zawsze zwracalo mocked_balance_value
        self.wallet_mock.get_balance.return_value = 10

        # wywołanie check_if_can_afford
        result = self.owner.check_if_can_afford(amount=cash_to_validate)

        # assercja czy owner moze sobie pozwolić na zakup
        assert result is False
        # assercja czy get_balance zostało wykonane
        self.wallet_mock.get_balance.assert_called_once()
