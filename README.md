# Rock-Paper-Scissors
AI Core Project 2 - Computer Vision Rock Paper Scissors 

The aim of project 2 is to create a rock/paper/scissors game in which a human player can play against the computer.
The computer takes a video feed of the human player's hand gesture which it recognises using a neural network.
It compares this to its own random selection of gesture to determine who has won any particular round with the
winner of the game being the player who has won the most out of a pre-determined number of rounds.

Milestone 2
In Milestone 2, a machine learning model is trained to recognise each of the three categories of rock, paper or scissors.
In addition, there is a fourth category of no gesture.
The model used is that provided on the Teachable Machine website which allows a non-specialist to train and download a
machine learning model. The model is suitable for the classification of three types of data: image, sound or pose.
In this case, image data is provided through the webcam with 1,000 frames being provided to show each of the gestures from
a wide range of angles. 200 training epochs were used with the training taking only a few minutes.
The model parameters are then downloaded so that it can be incorporated in the project code.

Milestone 3
In Milestone 3 a conda  environment vision was set up for the project using the  conda command, conda create --name vision python=3.8
For the project to work, the opencv-python and tensorflow libraries were installed in addition to the standard base environment.
Python 3.8 was required due to incompatibilities between Ubuntu and later versions of Python.

Milestone 4
In Milestone 4, a manual version of the game was created. The get_computer_choice function returns a random selection from the 3 possible game gestures.
get_user_choice takes keyboard input from the user.
And get_winner determines the winner using a nested dictionary encoding each of the 9 possible combinations of gestures. 
