import unittest

from src.deck import Deck


class TestDeck(unittest.TestCase):
    def test_deck_init(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_shuffle(self):
        deck = Deck()
        deck1 = str(deck.cards)
        deck.shuffle()
        deck2 = str(deck.cards)
        self.assertNotEqual(deck1, deck2)

    def test_deck_draw_size(self):
        deck = Deck()
        deck.draw()
        self.assertEqual(len(deck.cards), 51)

    def test_deck_draw_card(self):
        deck = Deck()
        first_card = deck.cards[-1].name
        card = deck.draw()
        self.assertEqual(card.name, first_card)

    def test_deck_draw_all(self):
        deck = Deck()
        for i in range(52):
            deck.draw()
        self.assertEqual(len(deck.cards), 0)
