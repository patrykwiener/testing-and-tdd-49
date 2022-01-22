"""
EXTRACT UPPERCASE LETTERS

Twoim zadaniem jest stworzenie funkcji zwracającej string zawierający wszystkie duże litery z podanego stringa.
String przyjmowany jest jako parametr 'sentence'. W pliku test_extract_uppercase_letters.py napisz testy tej funkcji.

Wskazówki:
*   Zalecam użycie pętli 'for' aby sprawdzić każdy ze znaków.
*   Do sprawdzenia czy dana litera jest wielką można użyć metody 'isupper()', która zwaraca True gdy litera jest wielka
    oraz False w przeciwnym wypadku. Np. <literka>.isupper().

"""


def extract_uppercase_letters(sentence):
    # upper_letters = ''
    #
    # for char in sentence:
    #     if char.isupper():
    #         upper_letters += char
    #
    # return upper_letters
    upper_letters_list = [char for char in sentence if char.isupper()]
    return ''.join(upper_letters_list)


if __name__ == '__main__':
    result = extract_uppercase_letters(sentence='Ala Ma Kota')
    print(result)
