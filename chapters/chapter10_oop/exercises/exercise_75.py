# Exercise 75 - Banking System [Part 2/2]
# So far we've defined the `Card` and `Account` classes. Now, let's define the `BankCustomer` class.


# The `BankCustomer` class should also have the following methods:
# 1. add_account(self, account: Account) -> None: adds an account to the accounts list.
# 2. remove_account(self, account_number: int) -> None: removes an account from the accounts list.
# 3. add_card(self, card: Card) -> None: adds a card to the cards list.
# 4. remove_card(self, card_number: int) -> None: removes a card from the cards list.
# 3. get_account(self, account_number: int) -> Account: returns an account based on the account number.
# 4. get_card(self, card_number: int) -> Card: returns a card based on the card number.
# 5. get_total_balance(self) -> float: returns the total balance of all accounts.
# 6. withdraw(self, account_number: int, amount: float, card_number: int, pin: int) -> None: withdraws money from an account.
# 7. deposit(self, account_number: int, amount: float) -> None: deposits money into an account.

# See `test_e75()` in `tests/test_ch10.py` for the expected behavior.

from .exercise_74 import Account, Card, Customer


class BankCustomer(Customer):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.accounts: list[Account] = []
        self.cards: list[Card] = []
        self.total_balance = 0.0

    def add_account(self, account: Account) -> None: ...

    def remove_account(self, account_number: int) -> None: ...

    def add_card(self, card: Card) -> None: ...

    def remove_card(self, card_number: int) -> None: ...

    def get_account(self, account_number: int) -> Account: ...

    def get_card(self, card_number: int) -> Card: ...

    def get_total_balance(self) -> float: ...

    def withdraw(
        self, account_number: int, amount: float, card_number: int, pin: int
    ) -> None: ...

    def deposit(self, account_number: int, amount: float) -> None: ...
