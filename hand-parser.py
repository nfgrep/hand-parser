# To make things a littler more readable
class Card:
  def __init__(self, face, suit):
    self.face = face
    self.suit = suit
  def __lt__(self,other):
    return self.face<other.face
  def __gt__(self,other):
    return self.face>other.face
  def __str__(self):
    return self.face + ":" + self.suit
  def __repr__(self):
    return str(self)

# The 5 cards that we are considering 
cards_dealt = [Card('2','d'),Card('A','d'),Card('2','s'),Card('A','d'),Card('A','d')]

face_counters = {'A': 0,
                 '2': 0,
                 '3': 0,
                 '4': 0,
                 '5': 0,
                 '6': 0,
                 '7': 0,
                 '8': 0,
                 '9': 0,
                 'T': 0,
                 'J': 0,
                 'K': 0}

suit_counters = {'d': 0,
                 'h': 0,
                 's': 0,
                 'c': 0}
