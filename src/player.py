class Player:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.bust = False
        self.blackjack = False

    def choose_ace_value(self):
        ace_value = input("Would you like your ace to be 1 or 11? ")
        if ace_value != "1" and ace_value != "11":
            print("Invalid input. Please try again.")
            self.choose_ace_value()
        else:
            self.score += int(ace_value)

    def add_card(self, card):
        self.hand.append(card)
        self.score += card.value
        if card.name.upper() == "ACE":
            self.choose_ace_value()
        if self.score > 21:
            self.bust = True
        if self.score == 21:
            self.blackjack = True
