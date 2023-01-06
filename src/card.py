names = ["JACK", "QUEEN", "KING", "ACE"]
numericNames = [n for n in range(2, 10)]

class Card:
    def __init__(self, name):
        self.name = name

        if self.name.isnumeric():
            self.value = int(self.name)
        elif self.name.upper() in names:
            self.value = 10
        elif self.name.upper() == "ACE":
            self.value = None
