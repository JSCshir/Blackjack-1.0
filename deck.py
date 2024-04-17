import random

play = [0]


class Uno:
    def __init__(self):
        self.hand = []

    def _get_random_card(self):
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        col = ["red", "blue", "green", "yellow"]
        return [random.choice(num), random.choice(col)]

    def deal(self):
        self.hand = [self._get_random_card() for _ in range(7)]

    def take(self):
        self.hand.append(self._get_random_card())

    def place(self, num):
        play.insert(0, self.hand.pop(num - 1))

    def __repr__(self):
        return f"{self.hand}"
