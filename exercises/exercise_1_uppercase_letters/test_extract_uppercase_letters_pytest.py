from exercises.exercise_1_uppercase_letters.extract_uppercase_letters import extract_uppercase_letters


def test_no_uppercase_letters():
    sentence = 'ala ma kota'
    expected = ''

    result = extract_uppercase_letters(sentence)

    assert result == expected


def test_empty_string():
    sentence = ''
    expected = ''

    result = extract_uppercase_letters(sentence)

    assert result == expected


def test_sentence_with_uppercase_letters():
    # deklaracji
    sentence = 'Ala Ma Kota'
    expected = 'AMK'

    # uruchomienia
    result = extract_uppercase_letters(sentence)

    # asercji
    assert result == expected
