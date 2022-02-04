from exercises.exercise_3_door_controller.door_controller import DoorController


class TestDoorController:

    def setup_method(self) -> None:
        self.door_controller = DoorController()

    def test_initially_door_is_closed(self):
        assert not self.door_controller.is_door_opened()

    def test_open_door(self):
        self.door_controller.open()

        assert self.door_controller.is_door_opened()

    def test_close_door(self):  # tu ostrożnie - pamiętajmy, że drzwi domyślnie są zamknięte
        # opening door
        self.door_controller.open()
        # closing door
        self.door_controller.close()

        assert not self.door_controller.is_door_opened()
