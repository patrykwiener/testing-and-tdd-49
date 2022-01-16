def test_sum():
    result = sum([1, 2, 3])
    assert result == 6, "Should be 6"


def test_sum_tuple():
    result = sum((1, 2, 2))
    assert result == 6, "Should be 6"


if __name__ == "__main__":

    # assert len([1, 2, 3]) == 3, "Should be 3"  # True
    # assert len([1, 2, 3]) == 2, "Should be 3"  # False -> AssertionError

    test_sum()
    test_sum_tuple()
    print("Everything passed")
