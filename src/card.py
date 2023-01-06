names = ["JACK", "QUEEN", "KING"]


class Card:
    def __init__(self, name, value=None):
        self.name = name

        if value is not None:
            self.value = value
        elif self.name.isnumeric():
            self.value = int(self.name)
        elif self.name.upper() in names:
            self.value = 10
        elif self.name.upper() == "ACE":
            self.value = None
