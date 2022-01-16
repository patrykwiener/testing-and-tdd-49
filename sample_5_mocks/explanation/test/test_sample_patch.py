import unittest
from unittest.mock import patch, MagicMock

from sample_5_mocks.explanation.sample_patch import RemovalService


class TestRemovalService(unittest.TestCase):

    @patch('sample_5_mocks.explanation.sample_patch.os')
    def test_rm(self, mock_os):
        # instantiate our service
        reference = RemovalService()

        reference.rm("any path")

        # test that the remove call was called.
        assert mock_os.remove.called, "Failed to not remove the file if not present."
        mock_os.remove.assert_called_once_with('any path')

    def test_rm(self):
        # instantiate our service
        reference = RemovalService()
        mock_os = MagicMock()

        with patch('sample_5_mocks.explanation.sample_patch.os', mock_os):
            reference.rm("any path")

            # test that the remove call was called.
            # self.assertTrue(mock_os.remove.called, "Failed to not remove the file if not present.")
            # lub
            mock_os.remove.assert_called_once_with('any path')

    def test_file_exists(self):
        # mockujemy modul os
        reference = RemovalService()
        mock_os = MagicMock()

        with patch('sample_5_mocks.explanation.sample_patch.os', mock_os):
            path = 'test/path'
            reference.file_exists(path)

            mock_os.path.exists.assert_called_once_with(path)
