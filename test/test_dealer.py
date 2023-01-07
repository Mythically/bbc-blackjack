import unittest
from src.dealer import Dealer
from src.card import Card
from src.deck import Deck


class TestDealer(unittest.TestCase):

    def test_ace_card(self):
        dealer = Dealer()
        dealer.hand = [Card("ACE"), Card("ACE")]
        dealer.check_hand_value()
        self.assertEqual(12, dealer.score)

    def test_ace_draw(self):
        dealer = Dealer()
        deck = Deck()
        deck.build()
        deck.shuffle()
        while "ACE" not in dealer.hand:
            dealer.add_card(deck.draw())
            print(list(str(card) for card in dealer.hand))
            print(dealer.score)