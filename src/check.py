from game import Game
from player import Player

player = Player('name', 'name@mail.com', '12345')
game = Game(1,10)

print(player.username)
print(player.wallet.balance)
player.wallet.debit(50)
print(player.wallet.balance)
player.logged_in = True
game.make_bet(player, 20)
print(player.wallet.balance)
game.make_bet(player, 20)
print(player.wallet.balance)
game.make_bet(player, 20)
print(player.wallet.balance)