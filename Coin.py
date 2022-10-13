import random

class Coin:
    options = ['heads', 'tails']
    #? class method vs instance method ??
    @classmethod
    def toss_coin(cls):
        return random.choice(cls.options)

#* SUPER COIN - CLAWS - PICK REGULAR COIN OR SUPER COIN ? 
