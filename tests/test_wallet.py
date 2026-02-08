import pytest
from src.exceptions import InsufficientFundsError
from src.wallet import Wallet


@pytest.fixture
def wallet():
    return Wallet()

def test_new_wallet_balance(wallet):
    assert wallet.balance == 0

@pytest.mark.parametrize('amount, expected_balance, expected_exception', [
    (100, 100, None),
    (50.34, 50.34, None),
    (0, None, ValueError),
    (-5, None, ValueError)
])
def test_wallet_debit(wallet, amount, expected_balance, expected_exception):
    if expected_balance is None:
        with pytest.raises(expected_exception):
            wallet.debit(amount)
    else:
        assert wallet.debit(amount) == expected_balance


@pytest.mark.parametrize('amount, expected_balance, expected_exception', [
    (50, 50, None),
    (50.34, 49.66, None),
    (0, None, ValueError),
    (-5, None, ValueError),
    (200, None, InsufficientFundsError)
])
def test_wallet_credit(wallet, amount, expected_balance, expected_exception):
    wallet.debit(100)
    if expected_balance is None:
        with pytest.raises(expected_exception):
            wallet.credit(amount)
    else:
        assert wallet.credit(amount) == expected_balance
