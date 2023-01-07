from src.player import Player


class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

    def deal_init(self, deck):
        for loop in range(2):
            self.add_card(deck.draw())
            if loop == 0:
                self.hand[0].set_hidden(True)

    def game_round(self, deck):
        self.hand[0].set_hidden(False)
        while self.score < 17:
            self.add_card(deck.draw())

    def add_card(self, card):
        self.hand.append(card)
        self.calculate_hand_score()
        self.check_player_state()

