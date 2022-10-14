import random

class Coin:
    options = ['heads', 'tails']
    #? class method vs instance method ??
    @classmethod
    def toss_coin(cls):
        return random.choice(cls.options)

    

#* SUPER COIN - CLAWS - PICK REGULAR COIN OR SUPER COIN ? 
class MegaCoin(Coin):
    options = ['heads', 'tails', "wings"]

# coin = MegaCoin()

# print(coin.toss_coin())


# def get_coin(coin_choice):
#     # print(coin_choice)
#     if coin_choice == 'coin':
#         return RegularCoin()
#     else:
#         return MegaCoin()