
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
  if Value == "Jack" or Value == "King" or Value == "Queen":
    ValueList.append(10) 
  elif Value == "Ace":
    ValueList.append(1)
    ValueList.append(11)
  else:
    ValueList.append(Value)
          
  return ValueList

#hand = [42, 23, 2, 51]
def get_hand_count(hand):
  possibleCounts= [0]
  countsPlusTen = []
  for i in range(len(hand)):
    card_value = card_to_value(hand[i]) # either [value] or [value, value]
    if len(card_value) == 1:
      for i in range (len(possibleCounts)):
        possibleCounts[i] += card_value[0]
    #if we pulled 11
    if len(card_value) == 2:
      for i in range (len(possibleCounts)):
        possibleCounts[i] += card_value[0]
        countsPlusTen.append(possibleCounts[i] + 10)
      for count in countsPlusTen:  
        possibleCounts.append(count)
  return possibleCounts




def print_hands():
  print("Player has", end=' ')
  for i in range(len(player_hand)):
    print((number_to_card(player_hand[i])) + ",", end=' ')
  
  print("")
  for i in range(len(dealer_hand)):
    print("Dealer has " +(number_to_card(dealer_hand[i])))
    
def is_hand_busted(hand):
  hand_value = get_hand_count(hand)
  #make a count variable and set to 0
  count = 0
  numhands = len(hand_value)
  for i in range(numhands):
    if hand_value[i] > 21:
      #add 1 to the count
      count += 1
  if count == len(hand_value):
    return True 
    print("hi")
  return False
    


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
deal_starting_hand(deck, player_hand,dealer_hand)

game_running =True
turn = "player"
while game_running:
  print_hands()

  print("Would you like to hit or stand?")
  hit_stand = input()
  #print(hit_stand)
  print(hit_stand)
  if hit_stand == "hit":
    if turn == "player":
      new_card(deck, player_hand)
      if is_hand_busted(player_hand) == True:
        print_hands()
        print("Player busted")
        game_running = False

    else:
      new_card(deck, dealer_hand)
      if is_hand_busted(dealer_hand) == True:
        print_hands()
        print("Dealer busted")
        game_running = False
  if hit_stand == "q":
    game_running = False
  # if the player types "s"
  if hit_stand == "s":
    #then set turn = "dealer"
    turn = "dealer"
    print("It is the "+ turn + "'s")
    #print whos turn it is
  
