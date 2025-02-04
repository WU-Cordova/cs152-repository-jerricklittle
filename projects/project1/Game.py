from Multideck import Multideck
from Card import Card
import random


class Game:
    def __init__(self):
        self.num_decks = random.choice(['2','4','6','8'])
        self.deck = Multideck(self.num_decks)
        self.player_hand = []
        self.dealer_hand = []

    def deal_initial_cards(self):
        # Method to deal the initial two cards to the player and dealer
        self.player_hand.append(self.deck.deal_card())
        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())

    def show_hands(self, hide_dealer_card):
        # Method to display the player's and dealer's hands
        # If hide_dealer_card is True, the dealer's second card is hidden
        print(f"Players deck is: {', '.join(str(card) for card in self.player_hand)}")
        if hide_dealer_card == True:
            print(f"Dealers hand is: {self.dealer_hand[0], 'HIDDEN'}")
        else:
            print(f"Dealers hand is: {', '.join(str(card) for card in self.dealer_hand)}")
    
    

    def calculate_hand_value(self, hand):
        # Method to calculate the total value of a hand (accounting for Aces)
        pass

    def player_turn(self):
        # Method to handle the player's turn (hitting or staying)
        pass

    def dealer_turn(self):
        # Method to handle the dealer's turn (drawing until reaching at least 17)
        pass

    def determine_winner(self):
        # Method to determine the winner of the round (player, dealer, or tie)
        pass

    def play_round(self):
        # Method to play a single round of the game
        pass

    def play_game(self):
        # Method to start the game and handle multiple rounds
        pass
