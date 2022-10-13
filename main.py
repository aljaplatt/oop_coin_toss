from Game import Game
from Coin import Coin
from Player import Player
from Game import play_game

def main():

    #* Set up player
    # player 1  inherit from comp class ??
    player = Player(input("Please enter your name: "))
    Computer = Player('Computer')

    #* set up game
    game = Game(player.name)
    coin = Coin()

    play_game(player, game, coin)
    
    #* Play game
# def play_game(player, game, coin):

#     while game.is_playing():
#         toss = coin.toss_coin()

#         player_choice = player.coin_choice()

#         game.update_score(player_choice, toss)

#         print(game.print_score(toss))
    
#     print(game.print_winner())




#? if this is a module, we only want to call it when we run main, not if it is imported
# safety - only run main if you run the file main from the cli
if __name__ == "__main__":
    main()