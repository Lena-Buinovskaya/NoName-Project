from src.exceptions import NotLoggedInError, IncorrectPasswordError
from src.wallet import Wallet
from src.api.api_client import ApiClient


class Player:
    def __init__(self):
        self.api_client = ApiClient()
        self.wallet = Wallet()
        self.logged_in = False
        self.profile = None
        self.user_id = None
        self.username = None

    def login(self, username, password):
        if not username or not password:
            raise ValueError('Fields cannot be empty')
        response = self.api_client.login(username, password)
        if response.status_code != 200:
            raise IncorrectPasswordError('Incorrect password')
        user = response.json()
        self.user_id = user['id']
        self.username = user['username']
        self.profile = user

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


player = Player()
player.login('emilys', 'emilyspass')
print(player.username)
print(player.user_id)
print(player.profile)
print(player.wallet.balance)
player.deposit(100)
print(player.wallet.balance)
