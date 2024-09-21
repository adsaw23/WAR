from card_attributes import card_val

class Card():
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = card_val[rank]
    def __str__(self):
        return f"{self.rank} of {self.suit}"