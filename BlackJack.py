import pygame
import random
deck = []

numbers_used = []

def check_used(num):
  for i in range(len(numbers_used)):
    if numbers_used[i] == num:
      return True

  return False

count = 0
while count < 52:
  random_num = random.randint(0,51)
  if check_used(random_num) == False:
    deck.append(random_num)
    numbers_used.append(random_num)
    count +=1 

print(deck)
print(len(deck))