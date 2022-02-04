import pytest

from exercises.exercise_5_investment_interest_counter.investment_interest_counter import InvestmentInterestCounter


class TestInvestmentInterestCounter:
    INTEREST_RATE = 0.01
    BALANCE = 10000

    def setup_method(self):
        self.account = InvestmentInterestCounter(self.INTEREST_RATE, self.BALANCE)

    @pytest.mark.parametrize('duration, expected_balance', [
        [0, 10000],
        [1, 10100],
        [2, 10201]])
    def test_yearly_capitalization(self, duration, expected_balance):
        account_balance = self.account.count_with_yearly_capitalization(duration)
        assert account_balance == expected_balance

    def test_yearly_capitalization_raises_exception(self):
        with pytest.raises(Exception):
            assert self.account.count_with_yearly_capitalization(-4)
