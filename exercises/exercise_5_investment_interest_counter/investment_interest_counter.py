"""
INVESTMENT INTEREST COUNTER

Naszym zaniem jest stworzenie kalkulatora liczącego sumę pieniędzy, którą dostaniemy na lokacie w określonym czasie.
Parametrami lokaty są oprocentowanie w skali rocznej oraz piędze które włożymy na lokatę.

Specyfikacja:
*   Atrybutami klasy są oprocentowanie lokaty (self._interest_rate) oraz piędze wkładane na lokatę (self._balance)
*   Metoda 'count_with_yearly_capitalization(duration)' zwraca sumę pieniędzy po upłynięciu lokaty w czasie określonym
    w parametrze 'duration'. Duration przedstawia liczbę lat trwania lokaty. Dla tej metody przyjmujemy, że
    kapitalizacja odsetek jest roczna (naliczanie odsetek następuje raz na rok).
*   Dodatkowo wymagane jest sprawdzanie czy w metodzie 'count_with_yearly_capitalization(duration)' duration nie
    jest mniejsze od zera. W takim przypadku rzucamy wyjątek DurationLessThenZero. Np. 'raise DurationLessThenZero()'


Napisz testy w pliku test_investment_interest_counter.py.
Szczególnie zwróć uwagę na przetestowanie wystąpienia wyjątku!!!
Użyj mechanizmu pokrycia kodu, aby sprawdzić czy wszystko zostało przetestowane.

"""


class DurationLessThenZero(Exception):
    pass


class InvestmentInterestCounter:
    def __init__(self, interest_rate, balance):
        self._interest_rate = interest_rate
        self._balance = balance

    def count_with_yearly_capitalization(self, duration):
        if duration < 0:
            raise DurationLessThenZero('Podano liczbę lat mniejszą od zera')
        else:
            balance = self._balance
            while duration > 0:
                balance += balance * self._interest_rate
                duration -= 1
            return balance
