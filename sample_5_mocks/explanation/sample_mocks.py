from unittest.mock import Mock, MagicMock

# class Sample:
#     def __init__(self):
#         self.sample_str = ...
#         self.sample_number = ...
#
#     def some_method(self):
#         pass

def mock1():
    # sample = Sample()
    # sample.sample_str
    # sample.sample_number
    #
    mock = Mock()
    mock.sample_str = 'sample_str'
    mock.sample_number = 10
    mock.some_method()
    t=0


def mock2():
    mock = Mock(return_value='mock_value')
    assert mock.return_value == 'mock_value'

    mock.some_method = Mock(return_value='mocked_method_value')
    assert mock.some_method() == 'mocked_method_value'

    mock.some_method()
    assert mock.some_method.call_count == 2


def mock3():
    mock = Mock()
    mock.method_with_exception = Mock(side_effect=Exception('some_msg'))
    mock.method_with_exception()  # raises Exception


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
    mock = MagicMock()

    mock('test', 123)
    mock.assert_called_with('123', 123)
