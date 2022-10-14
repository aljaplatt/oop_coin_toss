from Game import Game
from Coin import Coin, MegaCoin, get_coin
from Player import Player
from clear import clear

def main():

    #* Set up player
    # player 1  inherit from comp class ??
    while True:
        try:
            player = Player(input("Please enter your name: "))
            winning_num = int(input(f"Hey {player.name}, pick a number of games required to win: "))
            coin_choice = input("For the regular Coin, type 'Coin'. Or type 'Mega' for the Mega-Coin:  ")
        except ValueError:
                print("Missing value")
        else:
            if player and winning_num and coin_choice:
                clear()
                print(f"Great, first to {winning_num} correct guesses wins, lets go!")

                coin = get_coin(coin_choice)

                Game.start_game(player, winning_num, coin)
                break

    
#? if this is a module, we only want to call it when we run main, not if it is imported
# safety - only run main if you run the file main from the cli
if __name__ == "__main__":
    main()