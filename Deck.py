import random

class Deck:
	 """
	    A class representing a deck of playing cards.

	    Attributes:
	        suits (list): List of suits ('♠', '♥', '♦', '♣').
	        ranks (list): List of ranks ('A', '2', ..., 'K').
	        cards (list): List of all cards in the deck, shuffled.

	    Methods:
	        draw(no_of_cards): Draws a number of cards from the deck.
	        
    """
	def __init__(self, num_decks):
		self.suits = [ '♠', '♥', '♦', '♣' ];
		self.ranks = [ 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' ];
		self.cards = [s+r for s in suits for r in ranks] * num_decks
		random.shuffle(self.cards)

	def draw(no_of_cards):			
		drawnHand = ShuffledDeck[:no_of_cards];
		del ShuffledDeck[:no_of_cards]
		return drawnHand