from classes.Game import Game
from classes.c2 import MegaCoin, Coin, RandomCoin
from classes.Player import Player
from helper.clear import clear
from helper.art import coin_ascii
import sys


def main():

    clear()
    print(coin_ascii)
    print("Welcome to the official Coin Flip World Championships (CFWF)\n")

    while True:
        try:
            player = Player(input("Please enter your name: "))
            clear()
            winning_num = int(
                input(
                    f"Hey {player.name}, pick the number of correct guesses required to win: "
                )
            )

            while player.coin_choice not in Coin.coin_options:
                player.coin_choice = input(
                    " For the regular Coin, type 'coin'.\n For the mega Coin, type 'mega'. \n Or type 'random' for the Random-Coin.\n Type 'exit' to quit:  "
                ).lower()

                if player.coin_choice == "exit":
                    print("\nHave a great day!\n")
                    sys.exit(0)

                if player.coin_choice not in Coin.coin_options:
                    print(
                        "\nPlease type either 'coin' or 'mega, or 'exit' to quit the game."
                    )

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
                clear()
                print(
                    f"Great, the first to {winning_num} correct guesses wins, lets go!"
                )

                Game.start_game(player, winning_num, coin)
                break


if __name__ == "__main__":
    main()
