from exercises.exercise_4_guest_list.guest_list import GuestList


class TestGuestList:

    def setup_method(self):
        self.guest_list = GuestList()

    def test_get_guest_list_is_empty(self):  # przypadek gdy lista jest pusta
        expected = 'The list is empty'

        actual = self.guest_list.get_guest_list()

        assert expected == actual

    def test_add_list_adds_person(self):
        test_person = 'Leonardo DiCaprio'
        expected = [test_person]

        self.guest_list.add_guest(test_person)
        actual = self.guest_list.get_guest_list()

        assert expected == actual

    def test_added_person_is_invited(self):  # test dla is_person_invited() równego True
        test_person = 'Johnny Depp'

        self.guest_list.add_guest(test_person)
        result = self.guest_list.is_person_invited(test_person)

        assert result

    def test_added_person_is_not_invited(self):  # test dla is_person_invited() równego False
        test_person = 'Johnny Depp'
        not_invited_person = 'Britney Spears'

        self.guest_list.add_guest(test_person)
        result = self.guest_list.is_person_invited(not_invited_person)

        assert not result
