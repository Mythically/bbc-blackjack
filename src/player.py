class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.bust = False
        self.blackjack = False
        self.stand = False

    # def __str__(self):
    #     hand_string = ""
    #     for card in self.hand:
    #         hand_string += str(card.name) + ", "
    #     return hand_string

    def stands(self):
        self.stand = True

    def add_card(self, card):
        card.value = self.check_card_value(card)
        self.hand.append(card)
        self.score += card.value
        self.check_player_state()

    def check_card_value(self, card):
        if isinstance(card.name, str):
            if card.name.upper() == "ACE":
                return self.choose_ace_value(card).value
        return card.value

    def check_player_state(self):
        if self.score == 21:
            self.blackjack = True
        if self.score > 21:
            self.bust = True

    def choose_ace_value(self, card=None):
        ace_value = input("Would you like your ace to be 1 or 11? ")
        if ace_value != "1" and ace_value != "11":
            print("Invalid input. Please try again.")
            self.choose_ace_value()
        else:
            card.set_ace_value(int(ace_value))
            return card

    def player_can_continue(self):
        if self.bust:
            return False
        if self.blackjack:
            return False
        if self.stand:
            return False
        return True
