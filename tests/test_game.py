import random
import pytest
from src.exceptions import NotLoggedInError, InsufficientFundsError


@pytest.mark.regress
def test_not_logged_in_make_bet(game, player):
    with pytest.raises(NotLoggedInError):
        game.make_bet(player, 10)


@pytest.mark.regress
@pytest.mark.smoke
def test_losing_bet(monkeypatch, game, logged_in_player):
    logged_in_player.deposit(100)

    monkeypatch.setattr(random, 'choice', lambda x: False)

    result = game.make_bet(logged_in_player, 10)
    assert result['result'] == 'lose'
    assert result['multiplier'] == 0
    assert logged_in_player.wallet.balance == 90


@pytest.mark.regress
@pytest.mark.smoke
def test_winning_bet(monkeypatch, game, logged_in_player):
    logged_in_player.deposit(100)
    monkeypatch.setattr(random, 'choice', lambda x: True)
    monkeypatch.setattr(random, 'randint', lambda x, y: 10)

    result = game.make_bet(logged_in_player, 10)

    assert result['result'] == 'win'
    assert result['multiplier'] == 10
    assert result['win_amount'] == 100
    assert logged_in_player.wallet.balance == 190


@pytest.mark.regress
@pytest.mark.parametrize('amount, expected_exception', [
    (1000, InsufficientFundsError),
    (0, ValueError),
    (-10, ValueError),
])
def test_bet_errors(game, logged_in_player, amount, expected_exception):
    with pytest.raises(expected_exception):
        game.make_bet(logged_in_player, amount)
