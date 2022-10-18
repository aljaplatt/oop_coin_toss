from Game import Game
from c2 import get_coin, Coin
from Player import Player
from clear import clear
from art import coin_ascii
import sys

def main():
    
    new_coin = Coin()
    
    clear()
    print("Welcome to the official Coin Flip World Championships (CFWF)\n")
    print(coin_ascii)

    while True:
        try:
            # clear()
            # print("Welcome to the official Coin Flip World Championships (CFWF)\n")
            # print(coin_ascii)
            
            #* Instantiate player object 
            player = Player(input("Please enter your name: "))
            clear()
            winning_num = int(input(f"Hey {player.name}, pick a number of games required to win: "))

            #* ABSTRACTION ?? - is referencing an object property like this bad practice?
            #? should I have a method that returns this property? 
            # getter setter 
            while new_coin.coin_choice not in new_coin.coin_options:
                new_coin.coin_choice = input("For the regular Coin, type 'coin'. Or type 'mega' for the Mega-Coin:  ").lower()
                
                if new_coin.coin_choice == 'exit':
                    print("\nHave a great day!\n")
                    sys.exit(0)

                if new_coin.coin_choice not in new_coin.coin_options:
                        print("\nPlease type either 'coin' or 'mega, or 'exit' to quit the game.")

            #? Move get coin to inside coin class
            coin = get_coin(new_coin.coin_choice)

        except ValueError:
                print("Missing value")
        else:
            if player and winning_num and new_coin.coin_choice:
                clear()
                print(f"Great, first to {winning_num} correct guesses wins, lets go!")

                Game.start_game(player, winning_num, coin)
                break


if __name__ == "__main__":
    main()