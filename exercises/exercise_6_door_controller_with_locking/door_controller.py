"""
DOOR CONTROLLER WITH LOCKING

Na podstawie wczesniej stworzonej klasy DoorController stworzymy mechanizm ryglowania drzwi.


"""


class DoorLockedError(Exception):
    pass


class DoorController:

    def __init__(self):
        self._is_opened = False
        self._is_locked = False

    def is_door_opened(self):
        return self._is_opened

    def is_door_locked(self):
        return self._is_locked

    def open(self):
        if self._is_locked:
            raise DoorLockedError('The door is locked. Cannot open')
        else:
            self._is_opened = True

    def close(self):
        self._is_opened = False

    def lock(self):
        self.close()
        self._is_locked = True

    def unlock(self):
        self._is_locked = False
