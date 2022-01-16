import pytest


class TestSample:

    @pytest.mark.parametrize('value,expected', [
        [1, 1],
        [2, 2]
    ])
    def test_multiple_values(self, value, expected):
        assert value == expected
