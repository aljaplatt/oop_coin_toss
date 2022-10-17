from clear import clear
class Player:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name.title()
    

    @property
    def name(self):
    #? underscore = protected or private 
        print("getting name...")
        return self._name


    @name.setter
    def name(self, name):
        print("setting name...")
        self._name = name


    @classmethod
    def coin_choice(cls):
        # clear()
        return input('Guess the coin toss: ')
    

    def __str__(self):
        return f"The players name is... {self.name}"
    
    __repr__ = __str__


#* WILD CARD - WILL MAKE THE COMPUTER HAVE TO GUESS FROM THREE OPTIONS INSTEAD OF TWO 

