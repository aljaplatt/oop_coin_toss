

# class Computer:



class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    @classmethod
    def coin_choice(cls):
        return input('Choose heads or tails?: ')


#* WILD CARD - WILL MAKE THE COMPUTER HAVE TO GUESS FROM THREE OPTIONS INSTEAD OF TWO 

