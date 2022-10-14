import random

class Coin:
    def __init__(self):
        self.coin_choice = ''
        self.coin_options = ('coin', 'mega')
    #? class method vs instance method ??
    @classmethod
    def toss_coin(cls):
        return random.choice(cls.options)

    # @classmethod
    # def new(cls, coin):
    #     if coin == cls.__class__.__name__:
    #         return cls()

    # def get_coin(coin_choice):
    # # print(coin_choice)
    #     return new(cls)
    
class RegularCoin(Coin):
    options = ['heads', 'tails']

#* SUPER COIN - CLAWS - PICK REGULAR COIN OR SUPER COIN ? 
class MegaCoin(Coin):
    options = ['heads', 'tails', "wings"]

def get_coin(coin_choice):
    # print(coin_choice)
    # options = ('coin', 'mega')
    # if coin_choice not in options:
    #     return False
    if coin_choice == 'coin':
        return RegularCoin()
    else:
        return MegaCoin()


# def get_coin(coin_choice):
#     print(coin_choice)
#     if coin_choice == 'coin':
#         return Coin()
#     else:
#         return MegaCoin()


# class Coin:
#     def __init__(self):
#         self.options = ['heads', 'tails']
    
#     def toss_coin(self):
#         return random.choice(self.options)

# #* SUPER COIN - CLAWS - PICK REGULAR COIN OR SUPER COIN ? 
# class MegaCoin(Coin):
#     def __init__(self):
#         super().__init__()
#         self.options = ['heads', 'tails', "wings"]

# coin = MegaCoin()

# print(coin.toss_coin())