import unittest

from src.card import Card
from src.player import Player
from src.deck import Deck


class TestPlayer(unittest.TestCase):
    def test_player_init(self):
        player = Player("Myth")
        self.assertEqual(player.hand, [])
        self.assertEqual(player.score, 0)
        self.assertEqual(player.bust, False)
        self.assertEqual(player.blackjack, False)

    def test_player_choose_ace_value_1(self):
        player = Player("Myth")
        card = Card("ACE")
        player.add_card(card=card)
        self.assertEqual(player.score, 1)

    def test_player_choose_ace_value_11(self):
        player = Player("Myth")
        card = Card("ACE")
        player.add_card(card=card)
        self.assertEqual(player.score, 11)

    def test_player_add_card(self):
        player = Player("Myth")
        deck = Deck()
        deck.build()
        card = deck.cards[-1]
        player.add_card(deck.draw())
        self.assertEqual(player.hand, [card])
        self.assertEqual(player.score, card.value)

    def test_player_check_hand_value(self):
        player = Player("Myth")
        player.score = 21
        player.check_hand_value()
        self.assertEqual(player.blackjack, True)

    def test_player_str(self):
        player = Player("Myth")
        self.assertEqual(str(player.hand), "[]")

    def test_player_two_aces(self):
        player = Player("Myth")
        player.add_card(Card("ACE"))
        player.add_card(Card("ACE"))
        self.assertEqual(player.score, 12)

    def test_player_two_aces_nine(self):
        player = Player("Myth")
        player.add_card(Card("ACE"))
        player.add_card(Card("ACE"))
        player.add_card(Card(9))
        self.assertEqual(player.score, 21)