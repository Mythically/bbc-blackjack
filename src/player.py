class Player:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.bust = False
        self.blackjack = False

    def __str__(self):
        hand_string = ""
        for card in self.hand:
            hand_string.join(str(card.name) + " ")
        return hand_string

    # set ace_value to none for testing purposes
    # it shouldn't be a passed parameter
    def choose_ace_value(self, card=None):
        ace_value = input("Would you like your ace to be 1 or 11? ")
        if ace_value != "1" and ace_value != "11":
            print("Invalid input. Please try again.")
            self.choose_ace_value()
        else:
            card.set_ace_value(int(ace_value))
            return card

    def add_card(self, card):
        if isinstance(card.name, str):
            if card.name.upper() == "ACE":
                card = self.choose_ace_value(card)
        self.hand.append(card)
        self.score += card.value

        if self.score > 21:
            self.bust = True
        if self.score == 21:
            self.blackjack = True

    def check_hand_value(self):
        if self.score > 21:
            self.bust = True
        if self.score == 21:
            self.blackjack = True

