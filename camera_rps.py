"""
AI Core Project 2 - Rock, Paper, Scissors using Computer Vision model

"""
import cv2
from keras.models import load_model
import numpy as np
import time
import random
import pygame_functions as pf

def get_computer_choice():
    """ Function to return a random selection from Rock, Paper or Scissors"""
    return random.choice(["Rock", "Paper", "Scissors"])

def get_prediction(model):
    """ Function using the open-cv2 vision library to capture
        a video frame from the computer's camera which
        is then used as input to the pre-trained neural network
        downloaded from Teachable Machine
        The frame is captured after a 5 second delay for
        which a timing loop displaying a countdown is used
    """
    gestures = ["Rock", "Paper", "Scissors", "None"]
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    seconds_left = 5
    pf.pygame_display_text(str(seconds_left), 256, (200,200), True)
    # Timer loop giving countdown whilst displaying feed from camera
    while seconds_left > 0:
        start_time = time.time()
        
        while time.time()-start_time<1: 
            ret, frame = cap.read()    
            cv2.imshow('Player Gesture', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        seconds_left-=1

        pf.pygame_display_text(str(seconds_left), 256, (200,200), True)

    # Resize the captured frame to 224x224, normalise, and send to model for prediction
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image
    prediction = model.predict(data, verbose=False)
    
    # After the loop release the cap object and destroy all windows
    cap.release()
    cv2.destroyAllWindows()
    return(gestures[np.argmax(prediction[0])])

def play_game():
    """
    Function containing the main game loop
    Game variables are initialised
    Game loop runs until one of the players has scored 3 points
    For each round, the computer makes a random choice by calling get_computer_choice
    The human player's gesture is determined by calling the get_prediction function
    If the human player has made a recognised gesture then it is compared to
    the computer's choice and scores are updated and appropriate messages are displayed
    When the game loop exits, the winner is declared
    """
    
    # Loads the pre-trained model
    model = load_model('/home/nick/Documents/AICore/Vision-Model/keras_model.h5')
    
    # Dictionaries containing scoring tables and messages for each game outcome
    # Keys in top level score_dict represent the human player's gesture
    # Keys in the nested dictionaries represent the computer's gesture
    # Human loses: -1, Tie: 0, Human wins: 1
    score_dict = {"Rock":{"Rock":0,"Paper":-1,"Scissors":1}, "Paper":{"Rock":1,"Paper":0,"Scissors":-1}, "Scissors":{"Rock":-1,"Paper":1,"Scissors":0}}
    result_message_dict = {-1:"You lost.", 0:"It's a tie!", 1:"You won!"}
    
    computer_score = 0
    user_score = 0
    
    # Main loop - keep going until somebody has 3 points
    while computer_score < 3 and user_score < 3:
        pf.pygame_display_text("COMPUTER SCORE "+str(computer_score)+"     "+str(user_score)+str(" USER SCORE"), 64, (100,100), True)
        pf.pygame_display_text("Press SPACEBAR to continue", 64, (100,300), False)
        pf.pygame_wait_for_spacebar()
        
        computer_choice = get_computer_choice()
        user_choice = get_prediction(model)
        
        if user_choice == "None":
            pf.pygame_display_text("You didn't make a gesture - try again", 64, (100,100), True)
            time.sleep(3)
        else:
            # Determine the outcome with a lookup in the score_dict dictionary and display messages
            outcome = score_dict[user_choice][computer_choice]
            pf.pygame_display_text("COMPUTER PLAYS "+computer_choice+", USER PLAYS "+user_choice, 64, (100,100), True)
            pf.pygame_display_text(result_message_dict[outcome], 64, (100,300), False)
            time.sleep(3)
            # Uses score tables to update scores without if/then/else
            computer_score+=max(-outcome,0)
            user_score+=max(outcome,0)

    pf.pygame_display_text("And the winner is..."+("YOU!" if user_score==3 else "COMPUTER :-)"), 64, (100,100), True)
    pf.pygame_display_text("Press SPACEBAR to end", 64, (100,300), False)
    pf.pygame_wait_for_spacebar()

play_game()