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
