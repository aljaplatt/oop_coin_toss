class Game:
    # def __init__(self, winning_score):
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        #* ability to change winning score? 
        self.winning_score = 5
        self.winner = ''

    def is_playing(self):
        if self.player_score != self.winning_score and self.computer_score != self.winning_score:
            return True
    # def __str__():

    # Active player - simulate computer making a choice ?? 
    
    def update_score(self, player, toss):
        if player == toss:
            self.player_score += 1
        else:
            self.computer_score += 1
    
    # def print_final_score(self):
