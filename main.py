from Game import Game
from Coin import Coin
from Player import Player

def main():
    # player 1  inherit from comp class ??
    player_1 = Player(input("Please enter your name: "))
    Computer = Player('Computer')

    game = Game(player_1.name)
    coin = Coin()
    # print(coin.options)
    
    while game.is_playing():
        toss = coin.toss_coin()
        # print('COIN TOSS:', toss)

        player_choice = player_1.coin_choice()
        # print(player_choice)

        game.update_score(player_choice, toss)

        print(game.print_score(toss))
    
    print(game.print_winner())


#? if this is a module, we only want to call it when we run main, not if it is imported
# safety - only run main if you run the file main from the cli
if __name__ == "__main__":
    main()