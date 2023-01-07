import unittest
from src.dealer import Dealer
from src.card import Card
from src.deck import Deck


class TestDealer(unittest.TestCase):

    def test_dealer_one_ace(self):
        dealer = Dealer()
        dealer.hand = [Card("ACE")]
        dealer.calculate_hand_score()
        self.assertEqual(11, dealer.score)

    def test_dealer_two_aces(self):
        dealer = Dealer()
        dealer.hand = [Card("ACE"), Card("ACE")]
        dealer.calculate_hand_score()
        self.assertEqual(12, dealer.score)

    def test_dealer_one_ace_one_ten(self):
        dealer = Dealer()
        dealer.hand = [Card("ACE"), Card(10)]
        dealer.calculate_hand_score()
        self.assertEqual(21, dealer.score)

    def test_dealer_drawing(self):
        dealer = Dealer()
        deck = Deck()
        dealer.deal_init(deck)
        dealer.game_round(deck)
        self.assertTrue(dealer.score >= 17)
