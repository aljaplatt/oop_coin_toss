import random

class Coin:
    def __init__(self):
        self.coin_choice = ''
        self.coin_options = ('coin', 'mega')

    #? class method vs instance method ?? - static method? 
    @classmethod
    def toss_coin(cls):
        return random.choice(cls.options)


#* Regular and Mega are inheriting toss_coin method from Coin 

#? Change regular to random coin ??  
class RegularCoin(Coin):
    options = ['heads', 'tails']


#* POLYMORPHISM - HAVE GET_COIN METHOD RETURN DIFF COIN W/ DIFF OPTIONS
class MegaCoin(Coin):
    options = ['heads', 'tails', "wings"]


def get_coin(coin_choice):

    if coin_choice == 'coin':
        return RegularCoin()
    else:
        return MegaCoin()


