from unittest.mock import patch


class SomeClass:

    def something(self):
        return 'something'


if __name__ == '__main__':
    with patch.object(SomeClass, 'something', return_value='mock_msg') as mocked_something_method:
        assert SomeClass().something() == 'mock_msg'
        assert mocked_something_method.call_count == 1
        mocked_something_method.assert_called_once()

