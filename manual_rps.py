# AI Core Project 2 - Rock, Paper, Scissors
import random
import pygame

# Define colours and screen
X_MAX = 1000
Y_MAX = 1000

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

size = (X_MAX, Y_MAX)
screen = pygame.display.set_mode(size)


pygame.init()

def get_computer_choice():
    return random.choice("Rock", "Paper", "Scissors")

def get_user_choice():
    print("Please make your choice from R for Rock, P for Paper, and S for Scissors")
    while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "Rock"
                if event.key == pygame.K_p:
                    return "Paper"
                if event.key == pygame.K_s:
                    return "Scissors"

print(get_user_choice())
