"""
actions hit =get another card and stand =stop receiving cards

scenarios
player goes over 21 bust
comuuter does same
one of them doesnt go over win

Jack, queen and king = value 10
ace 11 or 1


"""
import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'King': 10, 'Queen': 10, 'Ace': 11}
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'King', 'Queen', 'Ace']

playing = True  # to control the game flow


class Card:
    def __init__(self, suit, rank):
        self.suit = suit  # Hearts, diamond, spades, clubs
        self.rank = rank  # one, two,..., Jack, Queen, King, Ace

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    """ Creating deck of 52 cards in a list using global variables suits and ranks. """

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.extend([f'{rank} of {suit}'])

    "Function for printing out a deck."

    def __str__(self):
        return f' Content of a deck is: {self.deck}'

    " Card shuffling method. "

    def shuffle(self):
        return random.shuffle(self.deck)

    "Method dealing a random card and printing out the output. "

    def deal(self):
        chosen_card = random.choice(self.deck)
        self.deck.remove(chosen_card)
        print(f'You received {chosen_card}')
        return chosen_card


test = Deck()
print(test)


class Hand:
    def __innit__(self):
        self.value = 0
        self.cards = []
        self.aces = 0

    def add_card(self, card):

        return self.cards.append(Deck.deal(self.deck))

    def __str__(self):
        return f'Your current deck is as follows: {self.cards}'


test_hand = Hand()
Hand.add_card(test_hand, Deck.deal(test) )




