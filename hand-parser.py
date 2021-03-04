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


## --- TODO:
## sorting dont work because we are using strings for everything
## can change everything to a numerical representation
## and use enums

# Sort our cards
cards_dealt.sort(reverse=True)
print("Cards dealt: ", cards_dealt)


# Count how many of each face and suit in dealt cards
for card in cards_dealt:
  face_counters[card.face] += 1
  suit_counters[card.suit] += 1


# Check for pairs, trips and quads
duplicates = {}

for face,count in face_counters.items():
  if count == 2:
    duplicates['pair'] = face
  elif count == 3:
    duplicates['trip'] = face
  elif count == 4:
    duplicates['quad'] = face

print("duplicates in hand: ", duplicates)
