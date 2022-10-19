from helper.clear import clear


class Player:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name.title()
        self.coin_choice = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def coin_choice(self):
        return self._coin_choice

    @coin_choice.setter
    def coin_choice(self, coin_choice):
        self._coin_choice = coin_choice

    @classmethod
    def prompt_coin_choice(cls):
        return input("Guess the coin toss: ")

    def __str__(self):
        return f"The players name is... {self.name}"

    __repr__ = __str__
