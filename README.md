# Rock-Paper-Scissors
AI Core Project 2 - Computer Vision Rock Paper Scissors 

The aim of project 2 is to create a rock/paper/scissors game in which a human player can play against the computer.
The computer takes a video feed of the human player's hand gesture which it recognises using a neural network.
It compares this to its own random selection of gesture to determine who has won any particular round with the
winner of the game being the player who has won the most out of a pre-determined number of rounds.

## Milestone 2
In Milestone 2, a machine learning model is trained to recognise each of the three categories of game gesture rock, paper or scissors.
plus a fourth category of no gesture.
The model used is that provided on the Teachable Machine website which allows a non-specialist to train and download a
machine learning model. The model is suitable for the classification of three types of data: image, sound or pose.
In this case, image data is provided through the webcam with 1,000 frames being provided to show each of the gestures from
a wide range of angles. 200 training epochs were used with the training taking only a few minutes.
The model parameters are then downloaded so that it can be incorporated in the project code.

## Milestone 3
In Milestone 3 a conda  environment vision was set up for the project using the  conda command, conda create --name vision python=3.8
For the project to work, the opencv-python and tensorflow libraries were installed in addition to the standard base environment.
Python 3.8 was required due to incompatibilities between Ubuntu and later versions of Python.

## Milestone 4
In Milestone 4, a manual version of the game was created.
get_computer_choice function returns a random selection from the 3 possible game gestures.
get_user_choice takes keyboard input from the user.
get_winner determines the winner using a nested dictionary encoding each of the 9 possible combinations of gestures.

## Milestone 5
Milestone 5 implements a game loop with countdown timer and scoring.

The Pygame library is used to display game messages with pygame code being placed
in a separate module for clarity.

Code for capturing the image from the camera and feeding it into the pre-trained model had been supplied.
The code uses a combination of the open-CV2 and tensorflow libraries to capture video from the camera
and determine the gesture from the pre-trained neural network. This formed the core of the get_prediction function.

There was initially a very noticeable lag on the video display. This was because the supplied code was scaling and
running the model over every video frame which made for a very poor game experience.

To solve this, the code outputting the video stream from the camera to the display was placed within a loop giving a countdown
but the model was fed with only the final frame of video immediately prior to the termination of the countdown loop.
Thus the scaling of the video frame and running the model is only done once.

The result was a function that gave a countdown for the player's gesture without laggy video.

The game logic is contained in the play_game function. Game variables (primarily scores and lookup tables) are
initialised. Within a while loop, the computer makes a random choice via a call to get_computer_choice and
the user's gesture is obtained by a call to get_prediction.

Gestures are compared to determine the winner for each round, scores are updated and game pauses execution until
spacebar is pressed. When either player scores 3 points, the game end.

## Improvements
The game satisfies the specification including some of the add-ons such as a countdown timer and pressing a key to continue.
Making a game class rather than defining it only using functions seems to be of limited benefit given that it wouldn't
make the stucture any simpler or clearer and the code itself would remain almost entirely the smae.

The primary improvement would be to re-train the initial neural network. Whilst it is good at recognising the gestures,
it often misinterprets no gesture as being a valid gesture. Training the network with a blank background would
most likely solve this.

![Screenshot from 2022-11-18 11-54-41](https://user-images.githubusercontent.com/63295424/202713218-41bfe91d-48d4-4216-9d64-ae00d0f856e2.png)


![Screenshot from 2022-11-18 11-57-42](https://user-images.githubusercontent.com/63295424/202713260-c50c1d6d-ce6f-40bb-b5aa-37cab282b786.png)

![Screenshot from 2022-11-18 13-15-55](https://user-images.githubusercontent.com/63295424/202713847-f6d4352e-cf00-44d9-9326-2a7edb7aef93.png)

![Screenshot from 2022-11-18 12-00-54](https://user-images.githubusercontent.com/63295424/202714020-f9cf090e-215c-4cfc-84bc-fb7ef28d0fef.png)

![Screenshot from 2022-11-18 12-07-33](https://user-images.githubusercontent.com/63295424/202714209-c11040a2-d0db-4f5e-9574-2c4dfc3c7e4c.png)
