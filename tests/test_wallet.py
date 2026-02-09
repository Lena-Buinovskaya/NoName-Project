import pytest
from src.exceptions import InsufficientFundsError
from src.wallet import Wallet


@pytest.fixture
def wallet():
    return Wallet()


@pytest.mark.regress
def test_new_wallet_balance(wallet):
    assert wallet.balance == 0


@pytest.mark.regress
@pytest.mark.parametrize('amount, expected_balance, expected_exception', [
    pytest.param(100, 100, None, marks=pytest.mark.smoke),
    (50.34, 50.34, None),
    (0, None, ValueError),
    (-5, None, ValueError)
])
def test_wallet_debit(wallet, amount, expected_balance, expected_exception):
    if expected_balance is None:
        with pytest.raises(expected_exception):
            wallet.debit(amount)
    else:
        wallet.debit(amount)
        assert wallet.balance == expected_balance


@pytest.mark.regress
@pytest.mark.parametrize('amount, expected_balance, expected_exception', [
    pytest.param(50, 50, None, marks=pytest.mark.smoke),
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
        wallet.credit(amount)
        assert wallet.balance == expected_balance
