from unittest.mock import patch, MagicMock


"""

Do mockowania funckji open zależy użyć ścieżki 'builtins.open'.

"""


class TestReadFileLines:

    def test_open_called_with_path_and_in_read_mode(self):
        # Chcemy sprawdzić czy funkcja open została wywołana raz oraz czy została z oczekiwanymi parametrami.
        # (podpowiedź: metoda assert_called_once_with)
        pass

    def test_file_closed_called(self):
        # Testujemy czy plik został zakmnięty (assert_called_once na metodzie <file>.close()). Oczywiście nadal
        # mockujemy funkcję open() dodając mockowanie zwracanej wartości.
        pass

    def test_returns_expected_lines(self):
        # Testujemy czy funkcja zwraca oczekiwaną wartość z pliku. Nadal mockujemy open()
        # oraz file. Musimy sprawić, aby readlines zwrocilo to co oczekujemy.
        pass
