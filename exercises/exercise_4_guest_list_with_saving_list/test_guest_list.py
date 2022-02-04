from unittest.mock import patch

from exercises.exercise_4_guest_list_with_saving_list.guest_list import GuestList


class TestGuestList:
    mock_target = 'builtins.open'

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

    def test_save_empty_list_to_file(self):
        file_path = 'test.txt'
        open_mode = 'w'

        writelines_expected_param = []

        with patch(self.mock_target) as mock_file_open:
            self.guest_list.save_to_file(file_path)

            mock_file_open.assert_called_once_with(file_path, open_mode)

            file_mock = mock_file_open.return_value.__enter__()
            file_mock.writelines.assert_called_once_with(writelines_expected_param)

    def test_save_list_to_file(self):
        # open params
        file_path = 'test.txt'
        open_mode = 'w'

        # writelines_params
        first_person = 'Antonio Banderas'
        second_person = 'Angelina Jolie'
        writelines_expected_param = [first_person + '\n', second_person + '\n']

        # adding guests
        self.guest_list.add_guest(first_person)
        self.guest_list.add_guest(second_person)

        # mocking open() function
        with patch(self.mock_target) as mock_file_open:
            self.guest_list.save_to_file(file_path)

            mock_file_open.assert_called_once_with(file_path, open_mode)

            file_mock = mock_file_open.return_value.__enter__()
            file_mock.writelines.assert_called_once_with(writelines_expected_param)
