import random

		
suits = ["Diamonds", "Clubs", "Hearts", "Spades"]

ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

deck = ["%s of %s" % (rank, suit) for rank in ranks for suit in suits]

random.shuffle(deck)

PLAYER_COUNT = 6
player1_hand = [deck.pop(), deck.pop()]
player2_hand = [deck.pop(), deck.pop()]
player3_hand = [deck.pop(), deck.pop()]
player4_hand = [deck.pop(), deck.pop()]
player5_hand = [deck.pop(), deck.pop()]
player6_hand = [deck.pop(), deck.pop()]


	

print (player1_hand)
	