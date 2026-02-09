from src.exceptions import InsufficientFundsError

class Wallet:
    def __init__(self, balance=0):
        self.balance = balance


    def debit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount


    def credit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough money")
        self.balance -= amount