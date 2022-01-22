from exercises.exercise_1_uppercase_letters.extract_uppercase_letters import extract_uppercase_letters


class TestExtractUppercaseLetters:
    def test_no_uppercase_letters(self):
        sentence = 'ala ma kota'
        expected = ''

        result = extract_uppercase_letters(sentence)

        assert result == expected

    def test_empty_string(self):
        sentence = ''
        expected = ''

        result = extract_uppercase_letters(sentence)

        assert result == expected

    def test_sentence_with_uppercase_letters(self):
        # deklaracji
        sentence = 'Ala Ma Kota'
        expected = 'AMK'

        # uruchomienia
        result = extract_uppercase_letters(sentence)

        # asercji
        assert result == expected
