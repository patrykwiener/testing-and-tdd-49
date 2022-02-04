"""

IS PRIME NUMBER

To zadanie ma imitować programowanie przy użyciu TDD. W pliku test_is_prime_number.py znajdują się testy dla funkcji
is_prime_number(number). Na podstawie tych testów należy stworzyć ciało funkcji is_prime_number(number). Specyfikację
należy odczytać z testów.

Wskazówka:
Prime number (liczba pierwsza) to liczba będąca większa od 1, która dzieli się tylko przez 1 oraz samą siebie.

"""


def is_prime_number(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
