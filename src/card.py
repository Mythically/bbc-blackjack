names = ["JACK", "QUEEN", "KING", "ACE"]
numericNames = [n for n in range(2, 11)]


class Card:
    def __init__(self, name):
        self.name = name

        if isinstance(self.name, int):
            self.value = int(self.name)
        elif self.name.upper() in names:
            self.value = 10
        elif self.name.upper() == "ACE":
            self.value = 0

    def __str__(self):
        return str(self.name)

    def set_ace_value(self, value):
        if self.name.upper() == "ACE":
            if value != 1 and value != 11:
                raise ValueError(f"Invalid value.")
            self.value = value
        else:
            raise ValueError("Card is not an \"ACE\"")