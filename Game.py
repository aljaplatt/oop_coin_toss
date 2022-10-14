from clear import clear
from art import coin_art, computer

class Game:
    # self gives you access to the current instance object
    def __init__(self, name, number):
        if not name:
            raise ValueError("Missing name")
        if not number:
            raise ValueError("The game needs a number to play to")
        self.player_name = name
        self.player_score = 0
        self.computer_score = 0
        #* ability to change winning score? 
        self.winning_score = number
        self.winner = ''
        self.active_player = 'player'
        

    #* Checks if player or computer has reached the winning score 
    def is_playing(self):
        if self.player_score != self.winning_score and self.computer_score != self.winning_score:
            return True

        
    def print_score(self, toss_result):
        clear()
        return f"The coin landed with {toss_result} facing up. The score is {self.player_name}: {self.player_score}, Computer: {self.computer_score}"

    
    def update_score(self, player_choice, toss):
        if player_choice == toss and self.active_player == 'player':
            self.player_score += 1
        #TODO: UPDATE TO REFLECT COMPUTER CHOICE 
        elif player_choice == toss and self.active_player == 'computer':
            self.computer_score += 1

    # ? ???
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
            return f"Bad luck, the computer has won."
    

    def start_game(player, num, coin):
        if len(coin.options) > 2:
            print(f"You chose the Mega Coin, your options are HEADS, TAILS or WINGS")
        else:
            print(f"You chose the regular coin, your options are HEADS or TAILS.")

        game = Game(player.name, num)
        #* Play game
        game.__play_game(player, coin)
        print(game.print_winner())

    # can only be called from method inside class - like above
    def __play_game(self, player, coin):
        while self.is_playing():

            # PLAYER TURN
            toss = coin.toss_coin()
            print('TOSS:', toss)
            print('AP:', self.active_player)
            if self.active_player == 'player':
            
                player_choice = player.coin_choice()
                self.update_score(player_choice, toss)
                self.active_player = 'computer'
                print('AP2:', self.active_player)
            else:
                computer_choice = coin.toss_coin()
                print(f"The computer guessed... {computer_choice}")
                self.update_score(computer_choice, toss)
                self.active_player = 'player'
                print('AP3:', self.active_player)

            print('TOSS:', self.print_score(toss))
            # if self.active_player == 'player':
            #     self.active_player = 'computer'
            # else:
            #     self.active_player == 'player'

            # # COMPUTER TURN
            # toss = coin.toss_coin()
            # computer_choice = self.computer_turn()
            # self.update_score(computer_choice, toss)
            # print(self.print_score(toss))
            # self.active_player = 'player'
        
