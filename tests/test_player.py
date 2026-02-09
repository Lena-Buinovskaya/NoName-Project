import pytest
from src.exceptions import IncorrectPasswordError, NotLoggedInError


@pytest.mark.regress
def test_player_not_logged_in(player):
    assert player.logged_in is False


@pytest.mark.regress
@pytest.mark.parametrize('username,password,expected_result,expected_exception', [
    pytest.param('test_user', '12345', True, None, marks=pytest.mark.smoke),
    ('test_user', '', None, ValueError),
    ('', '12345', None, ValueError),
    ('', '', None, ValueError),
    ('test_user', '123', None, IncorrectPasswordError),
])
def test_player_logged_in(player, username, password, expected_result, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            player.login(username, password)
    else:
        player.login('test_user', '12345')
        assert player.logged_in is expected_result


@pytest.mark.regress
@pytest.mark.smoke
def test_player_logout(logged_in_player):
    logged_in_player.logout()
    assert logged_in_player.logged_in is False


@pytest.mark.regress
@pytest.mark.smoke
def test_player_balance(logged_in_player):
    assert logged_in_player.get_balance() == 0


@pytest.mark.regress
def test_not_logged_in_player_balance(player):
    with pytest.raises(NotLoggedInError):
        player.get_balance()


@pytest.mark.regress
@pytest.mark.smoke
def test_player_deposit(logged_in_player):
    logged_in_player.deposit(100)
    assert logged_in_player.get_balance() == 100


@pytest.mark.regress
@pytest.mark.smoke
def test_player_withdraw(logged_in_player):
    logged_in_player.deposit(100)
    logged_in_player.withdraw(50)
    assert logged_in_player.get_balance() == 50


@pytest.mark.regress
def test_not_logged_in_player_deposit(player):
    with pytest.raises(NotLoggedInError):
        player.deposit(100)


@pytest.mark.regress
def test_not_logged_in_player_withdraw(player):
    with pytest.raises(NotLoggedInError):
        player.withdraw(50)
