class Game:
    # self gives you access to the current instance object
    # def __init__(self, winning_score):
    def __init__(self, name):
        self.player_name = name
        self.player_score = 0
        self.computer_score = 0
        #* ability to change winning score? 
        self.winning_score = 3
        self.winner = ''

    def is_playing(self):
        if self.player_score != self.winning_score and self.computer_score != self.winning_score:
            return True

    # def print_score(self):
        
    def print_score(self, toss_result):
        return f"The coin landed with {toss_result} facing up. The score is {self.player_name}: {self.player_score}, Computer: {self.computer_score}"

    # Active player - simulate computer making a choice ?? 
    
    def update_score(self, player, toss):
        if player == toss:
            self.player_score += 1
        else:
            self.computer_score += 1
    
    def print_winner(self):
        if self.player_score == self.winning_score:
            return f"{self.player_name}, you have won!"
        else:
            return f"Bad luck, the computer has won."
    
    def play_game(self, player, game, coin):

        while self.game.is_playing():
            toss = coin.toss_coin()

            player_choice = player.coin_choice()

            game.update_score(player_choice, toss)

            print(game.print_score(toss))
        
        print(game.print_winner())
    

