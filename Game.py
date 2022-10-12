class Game:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

    # def __str__():
    
    def update_score(self, player, toss):
        if player == toss:
            self.player_score += 1
        else:
            self.computer_score += 1
    
    # def print_final_score(self):
