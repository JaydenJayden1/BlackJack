
import random
import warnings


#lesson 2


player_hand = []
dealer_hand = []
suits = ["heart","spade","club","diamond"]
values = [2,3,4,5,6,7,8,9,10,"Jack","King","Queen","Ace"]

def new_card(deck,hand):
  hand.append(deck[0])
  deck.remove(deck[0])

def deal_starting_hand(deck, phand, dhand):
  new_card(deck, phand)
  #second card into player
  new_card(deck,phand)
  #1st card to dealer
  new_card(deck,dhand)
  #2nd card to dealer
  new_card(deck,dhand)









def number_to_card(number):
  SuitIndex = number // 13
  Suit = suits[SuitIndex]
  ValueIndex = number % 13
  Value = values[ValueIndex]

  return "The " + str(Value) + " of " + Suit + "s"

def card_to_value(card):
  ValueList = []
  ValueIndex = card % 13
  Value = values[ValueIndex]
  if Value == "Jack" or "King" or "Queen":
    ValueList.append(10) 
  elif Value == "Ace":
    ValueList.append(1)
    ValueList.append(11)
  else:
    ValueList.append(Value)
          
  return ValueList

#hand = [42, 23, 2, 51]
def get_hand_count(hand):
  count = 0
  for i in range(len(hand)):
    card_value = card_to_value(hand[i])
    for j in range(len(card_value)):
      count = count + card_value[j]
  return count
    


def generate_and_shuffle_deck():
  deck = []
  for i in range(52):
    deck.append(i)

  temp = 0
  for i in range(51):
    random_num = random.randint(i+1, 51)
    temp = deck[i]
    deck[i] = deck[random_num]
    deck[random_num] = temp
  
  return deck



deck = generate_and_shuffle_deck()
print(deck)
deal_starting_hand(deck, player_hand,dealer_hand)
print(deck)
print(player_hand[0])
print(dealer_hand[0])
print(player_hand[1])
print(dealer_hand[1])





