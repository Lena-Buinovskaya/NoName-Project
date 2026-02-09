import pytest
from src.player import Player
from src.game import Game


@pytest.fixture
def player():
    return Player('test_user', 'user@mail.com', '12345')


@pytest.fixture
def logged_in_player(player):
    player.login('test_user', '12345')
    return player


@pytest.fixture
def game():
    return Game(1, 10)
