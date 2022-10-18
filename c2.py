import random

class Coin:
    coin_options = ('coin', 'mega')
    
    def __init__(self):
        self.coin_choice = ''
        self.options = ['heads', 'tails']

    #? class method vs instance method ?? - static method? 
    
    def toss_coin(self):
        return random.choice(self.options)
    
    def get_coin():
        return Coin()


#* Regular and Mega are inheriting toss_coin method from Coin 

# #? Change regular to random coin ??  
# class RegularCoin(Coin):
#     options = ['heads', 'tails']


#* POLYMORPHISM - HAVE GET_COIN METHOD RETURN DIFF COIN W/ DIFF OPTIONS
class MegaCoin(Coin):
    def __init__(self):
        self.options = ['heads', 'tails', "wings"]


    def get_coin():
        return MegaCoin()


# def get_coin(coin_choice):
#     print('===PRINT=== GC:', coin_choice)
#     if coin_choice == 'coin':
#         return RegularCoin()
#     else:
#         return MegaCoin()


