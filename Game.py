class Game:
    # self gives you access to the current instance object
    # def __init__(self, winning_score):
    def __init__(self, name):
        self.player_name = name
        self.player_score = 0
        self.computer_score = 0
        #* ability to change winning score? 
        self.winning_score = 5
        self.winner = ''

    def is_playing(self):
        if self.player_score != self.winning_score and self.computer_score != self.winning_score:
            return True

    # def print_score(self):
        
    def print_score(self):
        return f"The score is {self.player_name}: {self.player_score}, Computer: {self.computer_score}"

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
    
