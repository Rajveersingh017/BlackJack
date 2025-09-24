from Deck import Deck
from Hand import Hand

def blackJack():
	"""
	    Play a game of Blackjack in the terminal.

	    The game works like this:
	    - You and the dealer each get two cards.
	    - You can choose to "hit" (take another card) or "stand" (keep your total).
	    - If you go over 21, you lose immediately.
	    - Once you stand, the dealer takes their turn. The dealer must keep drawing 
	      cards until they reach at least 17.
	    - Whoever is closer to 21 without going over wins. 
	      If both totals are the same, it’s a draw.

	    You’ll be asked:
	    - How many decks to use (between 2 and 6).
	    - Whether you want to hit or stand during your turn.

	    The game will print out your hand, the dealer’s hand, 
	    and announce the result at the end.
    """
	
	print ("------------------ Welcome to Black Jack. ------------------\nGet a sum higher than dealer and below 22 to win")
	
	no_of_decks = int(input("BlackJack is usualy played with 2 to 6 standard decks. How many decks would you like: "))
	
	print ("Dealer STANDS at soft 17")
	print ("\n.......\nLets Begin:\n.......\n")
	
	deck = Deck(no_of_decks)

	player = Hand()
	dealer = Hand()
	
	player.addCards(deck.draw(2))
	dealer.addCards(deck.draw(2))

	# print ("deck : ", deck.cards)
	print ("dealer : ",dealer.card_in_hand, "| Dealer total : ", dealer.getValue())
	print ("player : ", player.card_in_hand , "| Player total : ", player.getValue(), "\n")

	while player.getValue() <22:
		action = input("Hit or Stand? (h/s): ").lower()
		if action == 'h':
			player.addCards(deck.draw(1))
			print("Your hand:", player.card_in_hand , "| Player total : ", player.getValue())
		else:
			break
	
	if player.getValue() > 21:
		print("Player bust! Dealer wins.")
		return

	print("\nDealer's Turn:", dealer.card_in_hand, "| Dealer's current total : ", dealer.getValue())

	while dealer.getValue() < 17:
		dealer.addCards(deck.draw(1))

		print("Dealer hits:", dealer.card_in_hand,"| Dealer total : ", dealer.getValue())
		print("")

	if dealer.getValue() > 21:
		print("Dealer bust! Player wins.")
	elif dealer.getValue() > player.getValue():
		print("Dealer wins.")
	elif dealer.getValue() < player.getValue():
		print("Player wins.")
	else:
		print("Push (draw).")
blackJack()