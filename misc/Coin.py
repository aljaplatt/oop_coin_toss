import random


class Coin:
    def __init__(self):
        # ? coin choice in Player?
        self.coin_choice = ""
        self.coin_options = ("coin", "mega")
        self.options = ["heads", "tails"]

    # ? class method vs instance method ??
    # @classmethod
    def toss_coin(self):
        return random.choice(self.options)


class MegaCoin(Coin):
    def __init__(self):
        self.options = ["heads", "tails", "wings"]


# ? Put method in each COIN CLASS - change how it is accesses in main.py
def get_coin(coin_choice):
    if coin_choice == "coin":
        return Coin()
    else:
        return MegaCoin()

    # @classmethod
    # def new(cls, coin):
    #     if coin == cls.__class__.__name__:
    #         return cls()

    # def get_coin(coin_choice):
    # # print(coin_choice)
    #     return new(cls)


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
