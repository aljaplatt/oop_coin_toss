from Game import Game
from c2 import MegaCoin, Coin, RandomCoin
from Player import Player
from clear import clear
from art import coin_ascii
import sys


def main():
    
    clear()
    print(coin_ascii)
    print("Welcome to the official Coin Flip World Championships (CFWF)\n")

    
    while True:
        try:
            player = Player(input("Please enter your name: "))
            clear()
            winning_num = int(input(f"Hey {player.name}, pick a number of games required to win: "))

            while player.coin_choice not in Coin.coin_options:
                player.coin_choice = input(" For the regular Coin, type 'coin'.\n For the mega Coin, type 'mega'. \n Or type 'random' for the Random-Coin.\n Type 'exit' to quit:  ").lower()
                
                if player.coin_choice == 'exit':
                    print("\nHave a great day!\n")
                    sys.exit(0)

                if player.coin_choice not in Coin.coin_options:
                    print("\nPlease type either 'coin' or 'mega, or 'exit' to quit the game.")

            if player.coin_choice == "coin":
                coin = Coin.get_coin()
            elif player.coin_choice == "mega":
                coin = MegaCoin.get_coin()
            else:
                coin = RandomCoin.get_coin()
                print(coin.options)

        except ValueError:
                print("Missing value")
        else:
            if player and winning_num and player.coin_choice:
                print(f"Great, first to {winning_num} correct guesses wins, lets go!")

                #? player and coin objects passed in to  
                Game.start_game(player, winning_num, coin)
                break


if __name__ == "__main__":
    main()