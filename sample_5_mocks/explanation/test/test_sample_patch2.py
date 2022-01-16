import unittest
from unittest.mock import patch, MagicMock

from sample_5_mocks.explanation.sample_patch_2 import get_first_line_length


class TestGetFirstLineLength(unittest.TestCase):

    def test_get_first_line_length(self):
        function_mock = MagicMock(return_value='Byly sobie kurki trzy')

        with patch('sample_5_mocks.explanation.sample_patch_2.read_file_first_line', function_mock):
            path = 'test/path'
            result = get_first_line_length(path)
            self.assertEqual(result, 21)
            function_mock.assert_called_once_with(path)
