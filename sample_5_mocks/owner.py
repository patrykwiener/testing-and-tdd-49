from sample_5_mocks.wallet import Wallet


class Owner:

    def __init__(self, first_name: str, last_name: str, wallet: Wallet):
        self.first_name = first_name
        self.last_name = last_name
        self._wallet = wallet

    def supply_wallet(self, cash):
        self._wallet.add_cash(cash=cash)
        t=0

    def withdraw_money(self, amount: float):
        self._wallet.spend_cash(spending=amount)

    def check_if_can_afford(self, amount: float) -> bool:
        balance = self._wallet.get_balance()
        return amount <= balance


if __name__ == '__main__':
    wallet = Wallet(amount=100)
    owner = Owner(first_name='Patryk', last_name='Wiener', wallet=wallet)
    result = owner.withdraw_money(amount=50)
    owner.check_if_can_afford(amount=123.3)
    t=0