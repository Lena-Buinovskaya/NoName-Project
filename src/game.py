import random
from src.exceptions import NotLoggedInError, InsufficientFundsError


class Game:
    def __init__(self, min_multiplier, max_multiplier):
        self.min_multiplier = min_multiplier
        self.max_multiplier = max_multiplier

    def make_bet(self, player, bet_amount):
        if not player.logged_in:
            raise NotLoggedInError("Player must be logged in to play")
        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than 0")
        if bet_amount > player.wallet.balance:
            raise InsufficientFundsError("You don't have enough funds")

        player.wallet.credit(bet_amount)

        win = random.choice([True, False])
        if win:
            multiplier = random.randint(self.min_multiplier, self.max_multiplier)
            win_amount = multiplier * bet_amount
            player.wallet.debit(win_amount)

            return {'result': 'win', 'multiplier': multiplier, 'win_amount': win_amount}

        return {'result': 'lose', 'multiplier': 0, 'win_amount': 0}