class Hand():
	
	"""
	    A class representing the hand of a player or dealer in Blackjack.

	    Attributes:
	        card_in_hand (list): The list of cards currently held in the hand.

	    Methods:
	        add_cards(cards): Adds one or more cards to the hand.
	        get_value(): Returns the total value of the hand according to Blackjack rules.  
    """

	def __init__(self):
		self.card_in_hand = []

	def addCards(self, new_cards):
		if isinstance(new_cards,list):
			self.card_in_hand.extend(new_cards)
		else:
			self.card_in_hand.append(new_cards)

	def getValue(self):
		currentRank = '';
		value=0;
		ranks =[];
		
		for card in self.card_in_hand:
			currentRank = card[1:]
			match currentRank:
				case 'A':
					currentRank = 1
				case 'J':
					currentRank = 10
				case 'Q':
					currentRank = 10
				case 'K':
					currentRank = 10
				case _:
					currentRank = int(currentRank)

			value = value + currentRank
			ranks.append(currentRank)

		return value
		# return ranks,value

