from src.card import names, numericNames, Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def __str__(self):
        cards_string = []
        for card in self.cards:
            cards_string.append(str(card.name))
        return cards_string

    def build(self):
        for loop in range(4):
            for name in names:
                self.cards.append(Card(name))
            for name in numericNames:
                self.cards.append(Card(name))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()