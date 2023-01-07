names = ["JACK", "QUEEN", "KING", "ACE"]
numericNames = [n for n in range(2, 11)]


class Card:
    def __init__(self, name):
        self.name = name
        self.hidden = False
        if isinstance(self.name, int):
            self.value = int(self.name)
        elif self.name.upper() == "ACE":
            self.value = 0
        elif self.name.upper() in names:
            self.value = 10

    def __str__(self):
        if self.hidden:
            return "Hidden"
        return str(self.name)

    def set_ace_value(self, value):
        if self.name.upper() == "ACE":
            if value != 1 and value != 11:
                raise ValueError(f"Invalid value.")
            self.value = value
        else:
            raise ValueError("Card is not an \"ACE\"")

    def set_hidden(self, boolean):
        self.hidden = boolean
