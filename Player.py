# class Computer:

class Player:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
            # try:
            #     while not name:
            #         name = input("Please enter a name: ")
            # except ValueError:
            #     print("Missing name")
        self.name = name
        # self.score = 0

    @classmethod
    def coin_choice(cls):
        return input('Choose heads or tails?: ')


#* WILD CARD - WILL MAKE THE COMPUTER HAVE TO GUESS FROM THREE OPTIONS INSTEAD OF TWO 

