from src.exceptions import NotLoggedInError, IncorrectPasswordError
from src.wallet import Wallet


class Player:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.wallet = Wallet()
        self.logged_in = False

    def login(self, username, password):
        if not username or not password:
            raise ValueError('Fields cannot be empty')
        if password != self.password:
            raise IncorrectPasswordError('Incorrect password')
        self.logged_in = True

    def logout(self):
        self.logged_in = False

    def get_balance(self):
        if not self.logged_in:
            raise NotLoggedInError('Player is not logged in')
        return self.wallet.balance

    def deposit(self, amount):
        if not self.logged_in:
            raise NotLoggedInError('Player is not logged in')
        self.wallet.debit(amount)

    def withdraw(self, amount):
        if not self.logged_in:
            raise NotLoggedInError('Player is not logged in')
        self.wallet.credit(amount)