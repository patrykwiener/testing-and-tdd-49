def test_sum():
    result = sum([1, 2, 3])
    assert result == 6, "Should be 6"


def test_sum_tuple():
    result = sum((1, 2, 2))
    assert result == 6, "Should be 6"
