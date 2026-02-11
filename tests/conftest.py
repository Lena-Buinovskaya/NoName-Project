import pytest
from src.player import Player
from src.game import Game


@pytest.fixture
def player():
    return Player()


@pytest.fixture
def logged_in_player(player):
    player.login('emilys', 'emilyspass')
    return player


@pytest.fixture
def game():
    return Game(1, 10)
