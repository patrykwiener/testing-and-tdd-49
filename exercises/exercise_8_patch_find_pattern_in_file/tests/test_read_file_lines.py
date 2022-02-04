from unittest.mock import patch, MagicMock

from exercises.exercise_8_patch_find_pattern_in_file.file_reader import read_file_lines

"""

Do mockowania funckji open zależy użyć ścieżki 'builtins.open'.

"""


class TestReadFileLines:
    path = 'test_path'
    mock_target = 'builtins.open'

    def test_open_called_with_path_and_in_read_mode(self):
        # Chcemy sprawdzić czy funkcja open została wywołana raz oraz czy została z oczekiwanymi parametrami.
        # (podpowiedź: metoda assert_called_once_with)
        with patch(self.mock_target, MagicMock()) as open_func_mock:
            read_file_lines(self.path)
            open_func_mock.assert_called_once_with(self.path, 'r')

    def test_file_closed_called(self):
        # Testujemy czy plik został zakmnięty (assert_called_once na metodzie <file>.close()). Oczywiście nadal
        # mockujemy funkcję open() dodając mockowanie zwracanej wartości.
        file_obj = MagicMock()
        with patch(self.mock_target, return_value=file_obj):
            read_file_lines(self.path)
            file_obj.close.assert_called_once()

    def test_returns_expected_lines(self):
        # Testujemy czy funkcja zwraca oczekiwaną wartość z pliku. Nadal mockujemy open()
        # oraz file. Musimy sprawić aby readlines zwrocilo to co oczekujemy.
        expected_lines = ['Show', 'Time']
        file_obj = MagicMock()
        file_obj.readlines.return_value = expected_lines
        with patch(self.mock_target, return_value=file_obj):
            read_lines = read_file_lines(self.path)
            assert expected_lines == read_lines
