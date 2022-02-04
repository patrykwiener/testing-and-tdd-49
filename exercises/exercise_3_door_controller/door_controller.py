"""
DOOR CONTROLLER

Wyobraźmy sobie, że piszemy sterownik do kontroli drzwi. Drzwi mogą się otwierać, zamykać.

Specyfikacja:
*   Tworząc obiekt domyślnie stan drzwi (atrybut prywatny '_is_opened') jest równy False
*   Metoda 'is_door_opened' pozwalającą sprawdzić aktualny stan drzwi (czy są otwarte czy zamknięte). Zwraca wartość
    boolowską (True lub False)
*   Metoda 'open' otwiera drzwi poprzez odpowiednie ustawienie atrybutu '_is_opened'
*   Metoda 'close' zamyka drzwi analogicznie poprzez odpowiednie ustawienie atrybutu '_is_opened'

W pliku test_door_controller napisz testy.

"""


class DoorController:
    def __init__(self):
        self._is_opened = False

    def is_door_opened(self):
        return self._is_opened

    def open(self):
        self._is_opened = True

    def close(self):
        self._is_opened = False
