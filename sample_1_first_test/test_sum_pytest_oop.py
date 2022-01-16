class TestSumPyTest:

    def test_sum(self):
        result = sum([1, 2, 3])
        assert result == 6, "Should be 6"

    def test_sum_tuple(self):
        result = sum((1, 2, 2))
        assert result == 6, "Should be 6"
