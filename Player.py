from clear import clear
class Player:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name.title()
        # self.score = 0

    @classmethod
    def coin_choice(cls):
        # clear()
        return input('Guess the coin toss: ')


#* WILD CARD - WILL MAKE THE COMPUTER HAVE TO GUESS FROM THREE OPTIONS INSTEAD OF TWO 

