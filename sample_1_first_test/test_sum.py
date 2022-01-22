def test_sum():
    result = sum([1, 2, 3])
    assert result == 6, "Should be 6"


def test_sum_tuple():
    result = sum((1, 2, 2))
    assert result == 6, "Should be 6"


def get_uppercase_letters(sentence):
    uppercase_letters = ''
    ...
    return uppercase_letters


def test_string_not_empty():
    result = get_uppercase_letters('Ala Ma Kota')
    assert result == 'AMK'


def test_empty_string():
    result = get_uppercase_letters('ala ma kota')  # ''
    assert not result  # -> not False


def test_all_upper_letters():
    result = get_uppercase_letters('ALA MA KOTA')  # ''
    assert not result  # -> not False


if __name__ == "__main__":
    assert 6 == 6  # -> assert True
    # assert 5 == 6  # -> assert False
    assert 'a' == 'a'  # -> True
    # assert ''  # -> False
    # assert []  # -> False
    # assert 0  # -> False

    assert len([1, 2, 3]) == 3, "Should be 3"  # True
    assert len([1, 2, 3]) == 2, "Should be 3"  # False -> AssertionError

    test_sum()
    test_sum_tuple()
    print("Everything passed")
