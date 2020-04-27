import random

SUITS = ["DIAMONDS", "SPADES", "HEARTS", "CLUBS"]
VALUES = ["ACE", "TWO" , "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]

class Card:

    # Card constructor
    def __init__(self, suit, value):
      self.suit = suit
      self.value = value

    # Returns the suit of the card.
    def get_suit(self):
      return self.suit

    # Returns the value of the card.
    def get_value(self):
      return self.value

class Deck:

    # Creates a sorted deck of playing cards. 13 values, 4 suits.
    def __init__(self):
      self.cards = []
      for s in SUITS:
        for v in VALUES:
          self.cards.append(Card(s, v))

    # Returns the number of Cards in the Deck
    def num_cards(self):
      return len(self.cards)


    # Shuffles the deck of cards.
    def shuffle(self):
      for i in range(self.num_cards() - 1, 0, -1):
        r = random.randint(0, i)
        self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # Returns the top Card in the deck, then puts it back.
    def peek(self):
      return self.cards[0]


    # Draws and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self):
      return self.cards.pop(0)

    # Adds the input card to the deck. If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card):
      if (self.num_cards() < 52):
        self.cards.append(card)
        return
      print("Can't add more cards. Raise Exception")


    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self):
      for c in self.cards:
        print("Card: {} {}".format(c.suit, c.value))


d = Deck()
# d.print_deck()
d.shuffle()
d.print_deck()
# c = Card(SUITS[0], VALUES[0])
# print(c.get_suit(), c.get_value())
