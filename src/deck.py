from card import names, numericNames, Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for loop in range(4):
            for name in names:
                self.cards.append(Card(name))
            for name in numericNames:
                self.cards.append(Card(name))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)