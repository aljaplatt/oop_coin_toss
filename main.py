from Game import Game
from c2 import get_coin, Coin
from Player import Player
from clear import clear
from art import coin_ascii
import sys

def main():
    new_coin = Coin()
    #* Set up player
    # player 1  inherit from comp class ??
    while True:
        try:
            clear()
            print("Welcome to the official Coin Flip World Champioships (CFWF)\n")
            print(coin_ascii)
            player = Player(input("Please enter your name: "))
            winning_num = int(input(f"Hey {player.name}, pick a number of games required to win: "))

            #* ABSTRACTION ?? 
            while new_coin.coin_choice not in new_coin.coin_options:
                new_coin.coin_choice = input("For the regular Coin, type 'coin'. Or type 'mega' for the Mega-Coin:  ").lower()
                
                if new_coin.coin_choice == 'exit':
                    print("\nHave a great day!\n")
                    sys.exit(0)

                if new_coin.coin_choice not in new_coin.coin_options:
                        print("\nPlease type either 'coin' or 'mega, or 'exit' to quit the game.")

            coin = get_coin(new_coin.coin_choice)

        except ValueError:
                print("Missing value")
        else:
            if player and winning_num and new_coin.coin_choice:
                clear()
                print(f"Great, first to {winning_num} correct guesses wins, lets go!")

                Game.start_game(player, winning_num, coin)
                break

    
#? if this is a module, we only want to call it when we run main, not if it is imported
# safety - only run main if you run the file main from the cli
if __name__ == "__main__":
    main()