import pytest


class TestIsPrimeNumber:

    def test_less_or_equal_one_is_false(self):
        number = 1

        result = is_prime_number(number)
        assert result

    @pytest.mark.parametrize('not_prime_number', [
        [4], [6], [8], [9]
    ])
    def test_not_prime_numbers(self, not_prime_number):
        result = is_prime_number(not_prime_number)
        assert not result

    @pytest.mark.parametrize('prime_number', [
        [2], [3], [5], [7]
    ])
    def test_prime_numbers(self, prime_number):
        result = is_prime_number(prime_number)
        assert result
