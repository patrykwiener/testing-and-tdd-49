import pytest

from exercises.exercise_6_door_controller_with_locking.door_controller import DoorController, DoorLockedError


class TestDoorController:

    def setup_method(self):
        self.door_controller = DoorController()

    def test_initially_door_is_not_opened(self):
        result = self.door_controller.is_door_opened()

        assert not result

    def test_open_door_opens(self):
        self.door_controller.open()

        result = self.door_controller.is_door_opened()

        assert result

    def test_close_door_after_open_door(self):
        # opening door
        self.door_controller.open()
        # closing door
        self.door_controller.close()

        result = self.door_controller.is_door_opened()

        assert not result

    def test_initially_door_is_not_locked(self):
        # sprawdzić czy początkowo drzwi nie są zablokowanie (assertFalse lub assertTrue)
        result = self.door_controller.is_door_locked()

        assert not result

    def test_lock_door_closes_and_locks(self):
        # wazne aby pamietac ze drzwi najpierw musza byc otwarte!!!
        # testujemy czy drzwi po lock() są zamkniete i zablokowane
        # opening
        self.door_controller.open()
        assert self.door_controller.is_door_opened()

        # closing and locking
        self.door_controller.lock()

        result_opened = self.door_controller.is_door_opened()
        result_locked = self.door_controller.is_door_locked()

        assert not result_opened
        assert result_locked


    def test_unlock_door(self):
        # aby można było odblokowac drzwi muszą byc one najpierw zablokowane!!!
        # closing
        self.door_controller.lock()

        self.door_controller.unlock()
        result_locked = self.door_controller.is_door_locked()

        assert not result_locked

    def test_exception_on_opening_locked_doors(self):
        # Testujemy wystąpienie wyjątku. Polecam sprawdzić w prezentacji składnię!
        # Użyć rozwiązania z context managerem 'with'
        # Pamietaj ze trzeba zaimportowac wyjatek DoorLockedError
        # Pamietajmy ze najpierw musimy zablokowac drzwi, a potem dopiero probowac je otwierac
        self.door_controller.lock()

        with pytest.raises(DoorLockedError, match='The door is locked. Cannot open'):
            self.door_controller.open()
