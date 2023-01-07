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
        card.value = self.check_card_value(card)
        self.hand.append(card)
        self.score += card.value
        self.check_dealer_state()

    def check_card_value(self, card):
        if isinstance(card.name, str):
            if card.name.upper() == "ACE":
                if self.score + 11 > 21:
                    card.value = 1
                else:
                    card.value = 11
        return card.value

    def check_dealer_state(self):
        if self.score == 21:
            self.blackjack = True
        if self.score > 21:
            self.bust = True
