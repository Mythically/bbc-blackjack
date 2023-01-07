import unittest
from src.card import Card


class TestCard(unittest.TestCase):
    def test_card(self):
        card = Card("ACE")
        self.assertEqual(card.name, "ACE")
        self.assertEqual(card.value, 0)
        self.assertEqual(card.hidden, False)
