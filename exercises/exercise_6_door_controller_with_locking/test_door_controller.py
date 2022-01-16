import unittest

from exercises.exercise_3_door_controller_with_locking.door_controller import DoorController, DoorLockedError


class TestDoorController(unittest.TestCase):

    def setUp(self) -> None:
        self.door_controller = DoorController()

    def test_initially_door_is_not_opened(self):
        result = self.door_controller.is_door_opened()

        self.assertFalse(result, 'Initially door is not closed')

    def test_open_door_opens(self):
        self.door_controller.open()

        result = self.door_controller.is_door_opened()

        self.assertTrue(result, 'Door does not open')

    def test_close_door_after_open_door(self):
        # opening door
        self.door_controller.open()
        # closing door
        self.door_controller.close()

        result = self.door_controller.is_door_opened()

        self.assertFalse(result, 'Door does not close')

    def test_initially_door_is_not_locked(self):
        # sprawdzić czy początkowo drzwi nie są zablokowanie (assertFalse lub assertTrue)
        result = self.door_controller.is_door_locked()

        self.assertFalse(result, 'Initially door is not locked')

    def test_lock_door_closes_and_locks(self):
        # wazne aby pamietac ze drzwi najpierw musza byc otwarte!!!
        # testujemy czy drzwi po lock() są zamkniete i zablokowane
        # opening
        self.door_controller.open()
        self.assertTrue(self.door_controller.is_door_opened())

        # closing and locking
        self.door_controller.lock()

        result_opened = self.door_controller.is_door_opened()
        result_locked = self.door_controller.is_door_locked()

        self.assertFalse(result_opened, 'Door does not close')
        self.assertTrue(result_locked, 'Door does not lock')


    def test_unlock_door(self):
        # aby można było odblokowac drzwi muszą byc one najpierw zablokowane!!!
        # closing
        self.door_controller.lock()

        self.door_controller.unlock()
        result_locked = self.door_controller.is_door_locked()

        self.assertFalse(result_locked, 'Door does not unlock')

    def test_exception_on_opening_locked_doors(self):
        # Testujemy wystąpienie wyjątku. Polecam sprawdzić w prezentacji składnię!
        # Użyć rozwiązania z context managerem 'with'
        # Pamietaj ze trzeba zaimportowac wyjatek DoorLockedError
        # Pamietajmy ze najpierw musimy zablokowac drzwi, a potem dopiero probowac je otwierac
        self.door_controller.lock()

        with self.assertRaises(DoorLockedError, msg='Does not raise exception on opening locked doors'):
            self.door_controller.open()
