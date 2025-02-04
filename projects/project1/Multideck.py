import random
from Card import Card
class Multideck:
    def __init__(self, num_decks):
        self.num_decks = num_decks
        self.cards = self.create_deck()
        self.shuffle()
    def create_deck(self):
        suits = ['H', 'D', 'S', 'C']
        ranks = ['1','2','3','4','5','6', '7','8','9','10','J','Q','K']
        single_deck = [Card(suit,rank) for suit in suits for rank in ranks]
        return single_deck * self.num_decks
    def shuffle(self):
        random.shuffle(self.cards)
    def deal_card(self):
        return self.cards.pop()
