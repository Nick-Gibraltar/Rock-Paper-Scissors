# AI Core Project 2 - Rock, Paper, Scissors
import random
import pygame

# Define colours and screen
X_MAX = 1000
Y_MAX = 1000
SCORE_DICT = {"R":{"R":0,"P":-1,"S":1}, "P":{"R":1,"P":0,"S":-1}, "S":{"R":-1,"P":1,"S":0}}
RESULT_MESSAGE_DICT = {-1:"You lost.", 0:"It is a tie!", 1:"You won!"}

size = (X_MAX, Y_MAX)
screen = pygame.display.set_mode(size)

pygame.init()

def get_computer_choice():
    
    return random.choice(["R", "P", "S"])

def get_user_choice():
    print("Please make your choice from R for Rock, P for Paper, and S for Scissors")
    while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "R"
                if event.key == pygame.K_p:
                    return "P"
                if event.key == pygame.K_s:
                    return "S"

def get_winner(user_choice, computer_choice):
    print(f"You played {user_choice}, Computer played {computer_choice}")
    return RESULT_MESSAGE_DICT[SCORE_DICT[user_choice][computer_choice]]

def play():
    while True:
        print(get_winner(get_user_choice(), get_computer_choice()))

play()