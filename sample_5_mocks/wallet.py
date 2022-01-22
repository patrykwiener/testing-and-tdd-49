class InsufficientAmount(Exception):
    pass


class Wallet:
    bank = 'ING'

    def __init__(self, amount=0):
        self._balance = amount

    def _validate_operation(self, spending):
        if spending > self._balance:
            raise InsufficientAmount()

    def add_cash(self, cash):
        self._balance += cash

    def spend_cash(self, spending):
        self._validate_operation(spending)
        self._balance -= spending

    def get_balance(self):
        return self._balance
