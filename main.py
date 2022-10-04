from Coin import Coin
from Player import Player

coin = Coin()
# print(coin.options)

result = coin.toss_coin()

print(result)

# player 1  inherit from 
player_1 = Player(input("Please enter your name: "))
Computer = Player('Computer')

# print(player_1.name)