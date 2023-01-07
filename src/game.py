from src.deck import Deck
from src.player import Player
from src.dealer import Dealer
from src.utils import *


class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.build()
        self.deck.shuffle()
        self.dealer = Dealer()
        self.players = []

    def player_setup(self):
        player_count = int(input("How many players would you like to add?"))
        for loop in range(player_count):
            name = input(f"Please enter a name for player {loop + 1}: ")
            self.players.append(Player(name))
        self.players.append(self.dealer)

    def deal_init(self):
        for loop in range(2):
            for player in self.players:
                if player.name == "Dealer":
                    continue
                player.add_card(self.deck.draw())
            self.dealer.add_card(self.deck.draw())
            if loop == 0:
                self.dealer.hand[0].set_hidden(True)
        for player in self.players:
            print(f"{player.name}'s hand is {list(str(card) for card in player.hand)} with a score of {player.score}.")

    # ask each player if they want a card (hit) or not (stand)
    def deal_round(self):
        for player in self.players:
            if player.name == "Dealer":
                self.dealer.hand[0].set_hidden(False)
            while player.player_can_continue():
                # show player's hand and score before asking to hit or stand
                print_player(player)
                choice = input(f"{player.name}, would you like to hit or stand? ")
                if choice.lower() == "hit" or choice.lower() == "h":
                    player.add_card(self.deck.draw())
                    print(
                        f"{player.name}'s hand is {list(str(card) for card in player.hand)} with a score of {player.score}.")
                elif choice.lower() == "stand" or choice.lower() == "s":
                    player.stands()
                else:
                    print("Invalid input. Please try again.")
        self.dealer.game_round(self.deck)

    # collect all player stats and states, and determine winners, if all players and dealer bust, it's a tie(push)
    def check_winners(self):
        winners = []
        for player in self.players:
            if player.bust:
                continue
            if player.blackjack:
                winners.append(player)
                continue
            if player.score > self.dealer.score:
                winners.append(player)
                continue
            if player.score == self.dealer.score:
                winners.append(player)
                continue
        if len(winners) == 0:
            print("It's a push!")
        else:
            for winner in winners:
                print(f"{winner.name} wins with a score of {winner.score}!")
