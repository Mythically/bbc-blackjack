from src.deck import Deck
from src.player import Player
from src.dealer import Dealer


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
                choice = input(f"{player.name}, would you like to hit or stand? ")
                if choice.lower() == "hit" or choice.lower() == "h":
                    player.add_card(self.deck.draw())
                    print(f"{player.name}'s hand is {list(str(card) for card in player.hand)} with a score of {player.score}.")
                elif choice.lower() == "stand" or choice.lower() == "s":
                    player.stands()
                else:
                    print("Invalid input. Please try again.")
        self.dealer.game_round(self.deck)

    def check_winners(self):
        for player in self.players:
            if player.name == "Dealer":
                continue
            if player.bust:
                print(f"{player.name} busts with a score of {player.score}.")
            elif player.blackjack:
                print(f"{player.name} has blackjack!")
            elif self.dealer.bust:
                print(f"{player.name} wins with a score of {player.score}!")
            elif self.dealer.blackjack:
                print(f"{player.name} loses with a score of {player.score}.")
            elif self.dealer.score > player.score:
                print(f"{player.name} loses with a score of {player.score}.")
            elif self.dealer.score < player.score:
                print(f"{player.name} wins with a score of {player.score}!")
            else:
                print(f"{player.name} ties with a score of {player.score}.")