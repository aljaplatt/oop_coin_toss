class Game:
    # self gives you access to the current instance object
    # def __init__(self, winning_score):
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
        

    #* Checks if player or computer has reached the winning score 
    def is_playing(self):
        if self.player_score != self.winning_score and self.computer_score != self.winning_score:
            return True

        
    def print_score(self, toss_result):
        return f"The coin landed with {toss_result} facing up. The score is {self.player_name}: {self.player_score}, Computer: {self.computer_score}"

    
    def update_score(self, player, toss):
        if player == toss:
            self.player_score += 1
        #TODO: UPDATE TO REFLECT COMPUTER CHOICE 
        else:
            self.computer_score += 1


    def computer_turn(coin):
        return coin.toss_coin()


    def print_winner(self):
        if self.player_score == self.winning_score:
            return f"{self.player_name}, you have won!"
        else:
            return f"Bad luck, the computer has won."
    

    def start_game(player, num, coin):
        if len(coin.options) > 2:
            print(f"You chose the Mega Coin, your options are HEADS, TAILS or WINGS")
        else:
            print(f"You chose the regular coin, your options are HEADS or TAILS.")

        game = Game(player.name, num)
        #* Play game
        game.play_game(player, coin)
        print(game.print_winner())


    def play_game(self, player, coin):
        while self.is_playing():
            toss = coin.toss_coin()

            player_choice = player.coin_choice()
            self.update_score(player_choice, toss)
            #TODO: UPDATE TO REFLECT COMPUTER CHOICE 
            # computer_choice = self.computer_turn()
            # self.update_score(computer_choice, toss)

            print(self.print_score(toss))
        
