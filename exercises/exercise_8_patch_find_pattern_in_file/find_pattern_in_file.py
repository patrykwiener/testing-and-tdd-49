"""

FIND PATTERN IN FILE

Specyfikacja find_pattern_in_file:
*   do odczytu zawartosci pliku nalezy użyć funkcji read_file_lines(path) (z poprzedniego zadania)
*   funkcja zwraca True jeżeli w zwróconej liście stringów (zawartości pliku) znajduje się wzór podany przez parametr
    pattern. Zwraca False jeżeli wzór nie występuje w tym pliku.
    Np. lista ['abc', 'def'], pattern 'a' -> True;
    lista ['abc', 'def'], pattern 'z' -> False;
    lista ['byly sobie kurki trzy'], pattern 'kurki' -> True

Należy napisać testy tej funkcji w pliku test_find_pattern_in_file.py. Należy użyć konstrukcję
patch() aby zamockowac zewnetrzna funkcje read_file_lines(path).

"""


def find_pattern_in_file(pattern: str, path: str) -> bool:
    pass
