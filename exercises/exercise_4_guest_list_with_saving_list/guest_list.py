"""
GuestList with saving list

Naszym zadaniem jest rozwinąć funkcjalność klasy GuestList o możliwość zapisu listy gości do pliku:
* Stwórz metodę save_to_file, która jako parametr przyjmuje ścieżkę do pliku wyjściowego,
  do którego zapisze aktualną listę gości.
* Każdy gość powinien być w osobnej linijce
* Zalecam otwarcie pliku w trybie 'w' oraz użycie metody pliku writelines(), która przyjmuje
  listę stringów do zapisu

"""


class GuestList:

    def __init__(self):
        self._guest_list = []

    def get_guest_list(self):
        return self._guest_list if self._guest_list else 'The list is empty'

    def add_guest(self, person):
        self._guest_list.append(str(person))

    def is_person_invited(self, person):
        return person in self._guest_list

    def save_to_file(self, path):
        pass
