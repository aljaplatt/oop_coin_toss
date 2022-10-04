import random

class Coin:
    options = ['heads', 'tails']

    @classmethod
    def toss_coin(cls):
        return random.choice(cls.options)
