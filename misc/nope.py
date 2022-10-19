import random

class Coin:
    def __init__(self):
        self.coin_choice = ''
        self.coin_options = ('coin', 'mega')
        self.options = ['heads', 'tails']

    #? class method vs instance method ??
    # @classmethod
    def toss_coin(self):
        return random.choice(self.options)
    
    def __str__(self):
        # for option in self.options:
        return f"You chose the Mega Coin, your options are {self.options}"

class MegaCoin(Coin):
    def __init__(self):
        self.options = ['heads', 'tails', "wings"]


def get_coin(coin_choice):
    if coin_choice == 'coin':
        return Coin()
    else:
        return MegaCoin()