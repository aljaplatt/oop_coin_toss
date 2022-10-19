import random


class Coin:
    coin_options = ("coin", "mega", "random")

    def __init__(self):
        self.coin_choice = ""
        self.options = ["heads", "tails"]


    def toss_coin(self):
        return random.choice(self.options)

    def get_coin():
        return Coin()

class RandomCoin(Coin):
    def __init__(self):
        self.options = []

    def generate_options(self):
        options = ["sword", "fireball", "claws", "fangs"]

        for _ in range(3):
            random_option = random.choice(options)
            if random_option not in self.options:
                self.options.append(random_option)
                options.remove(random_option)

    def get_coin():
        coin = RandomCoin()
        coin.generate_options()
        return coin

class MegaCoin(Coin):
    def __init__(self):
        self.options = ["heads", "tails", "wings"]

    def get_coin():
        return MegaCoin()
