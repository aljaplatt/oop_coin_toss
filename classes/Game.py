from helper.art import coin_art, computer
import time

class Game:
    def __init__(self, name, number):
        if not name:
            raise ValueError("Missing name")
        if not number:
            raise ValueError("The game needs a number to play to")
        self.player_name = name
        self.player_score = 0
        self.computer_score = 0
        # * ability to change winning score?
        self.winning_score = number
        self.active_player = "player"

    def start_game(player, num, coin):
        if len(coin.options) > 2:
            print(f"You chose the Mega Coin, your options are HEADS, TAILS or WINGS")
        elif "heads" not in coin.options:
            print(
                f"You chose the Random Coin, GOOD LUCK!.\nYour options could be SWORD, FIREBALL, CLAWS or FANGS"
            )
        else:
            print(f"You chose the regular coin, your options are HEADS or TAILS.")

        
        game = Game(player.name, num)
        game.__play_game(player, coin)
        print(game.print_winner())

    def __play_game(self, player, coin):
        while self.is_playing():

            toss = coin.toss_coin()

            if self.active_player == "player":
                player_coin_choice = player.prompt_coin_choice()
                self.update_score(player_coin_choice, toss, self.active_player)
            else:
                computer_choice = coin.toss_coin()
                print(f"The computer guesses...")
                time.sleep(1)
                print(f"... {computer_choice}")
                self.update_score(computer_choice, toss, self.active_player)
            time.sleep(1)
            self.switch_active_player()

            time.sleep(1)
            print("TOSS:", self.print_score(toss))
            time.sleep(2)

    def switch_active_player(self):
        if self.active_player == "player":
            self.active_player = "computer"
        else:
            self.active_player = "player"

    # * Checks if player or computer has reached the winning score
    def is_playing(self):
        if (
            self.player_score != self.winning_score
            and self.computer_score != self.winning_score
        ):
            return True

    def print_score(self, toss_result):
        return f"The coin landed with {toss_result} facing up. The score is {self.player_name}: {self.player_score}, Computer: {self.computer_score}"

    def update_score(self, player_choice, toss, active_player):
        if player_choice == toss and active_player == "player":
            self.player_score += 1
        elif player_choice == toss and active_player == "computer":
            self.computer_score += 1

    def computer_turn(coin):
        guess = coin.toss_coin()
        print(f"The computer guesses... {guess}")
        return guess

    def print_winner(self):
        if self.player_score == self.winning_score:
            print(coin_art)
            return f"{self.player_name}, you have won!"
        else:
            print(computer)
            return f"Bad luck {self.player_name}, the computer has won 😤."
