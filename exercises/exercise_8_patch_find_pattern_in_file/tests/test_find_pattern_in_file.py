from unittest.mock import patch, MagicMock

from exercises.templates.exercise_8_patch_find_pattern_in_file.find_pattern_in_file import find_pattern_in_file


class TestFindPatternInFile:

    def test_false_on_empty_file(self):
        # Przetestujmy sytuacje gdy odczytywany plik jest pusty. Funkcja powinna zwrócić False. Wewnętrzna funkcja
        # read_file_lines() w tym przypadku powinna zwróć pustą listę [].
        # Aby to osiągnąc bez otwierania rzeczywistego pliku musimy użyć konstrukcji patch().
        # Aby stworzyć atrapę wewnętrznej funkcji musimy podać do niej ścieżkę np.:
        # <folder>.<folder>.find_pattern_in_file.read_file_lines
        # Aby uzycie atrapy zwracało oczekiwaną wartość musimy stworzyć MagicMock'a w następujący sposób:
        # MagicMock(return_value=<jakas wartosc>).
        # Tak stworzony mock musi byc przekazany jako parametr do funkcji patch.
        # Jako podpowiedz patch ma być użyte z context managerem 'with'.
        # Chcemy także sprawdzić czy stworzony mock został wywołany, do tego celu użyjemy metody
        # Mock'a assert_called_once_with(value).

        read_file_lines_return_value = []
        # tworzymy mocka
        # read_file_lines_mock =

        # sciezke należy sobie samemu zmodyfikowac
        # with patch('exercises.templates.exercise_8_patch_find_pattern_in_file.find_pattern_in_file.read_file_lines',
        #            read_file_lines_mock):

        # sample_path = scieżka do pliku moze byc dowolna, wazne ze string

    def test_false_on_file_not_containing_pattern(self):
        # Testujemy sytuację gdy odczytywany plik nie posiada oczekiwanego wzoru. Funkcja powinna zwrócić False.
        # Należy użyc podobnej konstrukcji co w poprzednim przypadku testowym, tylko w tym przypadku mock bedzie zwracal
        # inna wartosc
        pass

    def test_true_on_file_containing_pattern(self):
        # Testujemy sytuację gdy odczytywany plik posiada oczekiwanego wzoru. Funkcja powinna zwrócić True. Również
        # posługujemy się podobną konstrukcją mocka poprzez patch().
        pass
