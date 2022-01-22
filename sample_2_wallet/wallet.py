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


if __name__ == '__main__':
    empty_wallet = Wallet()
    wallet = Wallet(amount=200)

    wallet.add_cash(cash=100)
    wallet.spend_cash(spending=50)
    wallet.spend_cash(spending=5000)
    print(wallet.get_balance())

    # print('Ala ma kota')
    # raise InsufficientAmount()

    # 1 / 0
    # val = 0
    #
    # if val == 0:
    #     raise ZeroDivisionError()
