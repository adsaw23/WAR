import random
import card_class as cd

class Deck():
    def __init__(self):
        self.all_cards = []
        for x in cd.rank:
            for y in cd.suits:
                self.all_cards.append(cd.Card(x,y))
    def shuffle_deck(self):
            random.shuffle(self.all_cards)
    def deal_one(self):
            return self.all_cards.pop()
