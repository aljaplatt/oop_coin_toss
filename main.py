from Game import Game
from Coin import Coin
from Player import Player

def main():
    game = Game()
    coin = Coin()
    # print(coin.options)

    # player 1  inherit from 
    player_1 = Player(input("Please enter your name: "))
    Computer = Player('Computer')
    # print(player_1.name)
    while not game.is_game_over:
        toss = coin.toss_coin()
        print('COIN TOSS:', toss)

        player_choice = player_1.coin_choice()
        print(player_choice)

        game.update_score(player_choice, toss)

        print("Ply: ", game.player_score)
        print('Com: ', game.computer_score)

#? if this is a module, we only want to call it when we run main, not if it is imported
# safety - only run main if you run the file main from the cli
if __name__ == "__main__":
    main()