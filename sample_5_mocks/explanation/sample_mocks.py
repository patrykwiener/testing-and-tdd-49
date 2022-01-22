from unittest.mock import Mock, MagicMock


class Sample:
    def __init__(self):
        self.sample_str = 'ala ma kota'
        self.sample_number = 123

    def some_method(self):
        pass


def mock1():
    sample = Sample()
    sample.sample_str
    sample.sample_number
    sample.some_method()

    mock = Mock()
    mock.sample_str = 'sample_str'
    mock.sample_number = 10
    mock.some_method()
    t = 0


def mock2():
    # 1
    # mock = Mock(return_value='ala_ma_kota')
    # 2
    mock = Mock()
    mock.return_value = 'ala_ma_kota'
    assert mock() == 'ala_ma_kota'
    assert mock.return_value == 'ala_ma_kota'

    mock = Mock()
    # 1
    # mock.some_method = Mock(return_value='mocked_method_value')
    # 2
    mock.some_method.return_value = 'mocked_method_value'
    print(mock.some_method())
    assert mock.some_method() == 'mocked_method_value'

    assert mock.some_method.call_count == 2
    t=0

def mock3():
    mock = Mock()
    mock.method_with_exception = Mock(side_effect=ZeroDivisionError('some_msg'))
    mock.method_with_exception()  # raises ZeroDivisionError


def magic_mock1():
    magic_mock = MagicMock()
    magic_mock.sample_str = 'sample_str'
    magic_mock.sample_number = 10
    magic_mock.some_method()

    assert magic_mock.__len__() == 0
    assert len(magic_mock) == 0


if __name__ == '__main__':
    mock1()
    mock2()
    # mock3()
    magic_mock1()
    b = Mock()
    mock = Mock()

    mock.some_method.return_value = 'Ala ma kota'
    mock.some_method()
    mock.some_method.assert_called_once_with()
