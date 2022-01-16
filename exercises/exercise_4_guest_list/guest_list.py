"""
GUEST LIST

Wyobraźmy sobie, że tworzymy elektroniczną listę gości, których zapraszamy na naszą wystrzałową imprezę!
Do listy można dodawać gości oraz sprawdzać czy dana osoba już na niej jest.
(dla uproszczenia pominiemy sprawę związaną z usuwaniem nazwisk)

Specyfikacja:
*   początkowo lista gości jest pusta
*   Goście przechowywani są jako string z imieniem i nazwiskiem. Np. 'Leonardo DiCaprio'.
*   metoda 'get_guest_list' zwraca nam aktualną listę gości. UWAGA!!! W sytuacji gdy lista jest pusta zwracany jest
    string 'The list is empty'.
*   metoda 'add_guest(person)' dodaje przekazaną osobę do listy
*   metoda 'is_person_invited(person)' zwraca True gdy podana osoba jest już na liście oraz False w przeciwnym wypadku.
    Zaleca się użycie specjalnego operatora, który prawdopodobnie był omawiany przy listach.

W pliku test_guest_list.py napisz testy dla tej klasy.
Sprawdź za pomocą narzędzia coverage czy pokryte zostały wszystkie przypadki.

"""


class GuestList:
    pass
