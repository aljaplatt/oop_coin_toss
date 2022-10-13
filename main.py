from Game import Game
from Coin import Coin
from Player import Player


def main():

    #* Set up player
    # player 1  inherit from comp class ??
    player = Player(input("Please enter your name: "))
    # Computer = Player('Computer')

    #* set up game
    game = Game(player.name)
    coin = Coin()

    #* Play game
    game.play_game(player, game, coin)
    print(game.print_winner())

    
#? if this is a module, we only want to call it when we run main, not if it is imported
# safety - only run main if you run the file main from the cli
if __name__ == "__main__":
    main()