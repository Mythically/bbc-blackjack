import unittest

from src.card import Card
from src.game import Game
from src.player import Player


class TestScenarios(unittest.TestCase):

    # play a game, 1 player
    def test_scenario_one(self):
        game = Game()
        game.player_setup()
        game.deal_init()
        self.assertEqual(2, len(game.players[0].hand))

    def test_scenario_two_part_one(self):
        game = Game()
        game.player_setup()
        game.deal_init()
        game.deal_round()
        self.assertTrue(3, len(game.players[0].hand))

    def test_scenario_two_part_two(self):
        game = Game()
        game.player_setup()
        game.deal_init()
        init_score = game.players[0].score
        game.deal_round()
        updated_score = game.players[0].score
        self.assertTrue(updated_score != init_score)

    def test_scenario_three(self):
        game = Game()
        game.player_setup()
        game.deal_init()
        game.deal_round()
        self.assertEqual(2, len(game.players[0].hand))

    def test_scenario_four_part_one(self):
        player = Player("Myth")
        player.add_card(Card("ACE"))
        player.add_card(Card("KING"))
        self.assertTrue(player.score <= 21)

    def test_scenario_four_part_two(self):
        player = Player("Myth")
        player.add_card(Card("ACE"))
        player.add_card(Card("KING"))
        self.assertFalse(player.bust)

    def test_scenario_five_part_one(self):
        player = Player("Myth")
        player.add_card(Card("KING"))
        player.add_card(Card("KING"))
        player.add_card(Card(2))
        self.assertTrue(player.score >= 22)

    def test_scenario_five_part_two(self):
        player = Player("Myth")
        player.add_card(Card("ACE"))
        player.add_card(Card("KING"))
        player.add_card(Card(2))
        self.assertTrue(True, player.bust)

    def test_scenario_five_part_three(self):
        player = Player("Myth")
        player.add_card(Card("ACE"))
        player.add_card(Card("KING"))
        player.add_card(Card(2))
        self.assertFalse(player.player_can_continue())

    def test_scenario_six(self):
        player = Player("Myth")
        player.add_card(Card("ACE"))
        player.add_card(Card("KING"))
        self.assertEqual(21, player.score)

    def test_scenario_seven(self):
        player = Player("Myth")
        player.add_card(Card("ACE"))
        player.add_card(Card("KING"))
        player.add_card(Card("QUEEN"))
        self.assertEqual(21, player.score)

    def test_scenario_eight(self):
        player = Player("Myth")
        player.add_card(Card("ACE"))
        player.add_card(Card(9))
        player.add_card(Card("ACE"))
        print(player.score)
        self.assertTrue(player.blackjack)