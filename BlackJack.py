import pygame
import random
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message="pkg_resources is deprecated")

pygame.init()
width, height = 800, 600 
screen = pygame.display.set_mode((width, height))

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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.display.flip() 

pygame.quit()
