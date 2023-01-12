# Computer Vision RPS
Milestone 1 - task 1:
I have set up GitHub and created a GitHub repo to track my code and save them onine whilst creating the Computer Vision Rock Paper Scissors game.

Milestone 2 - task 1:
In this task I had to create an image project model with 4 different classes that would be a part of a game - Rock, Paper, Scissors and Nothing. The "Nothing" class will present the lack of movement. The model that I used to create these 4 classes is a web-based tool called Teachable-Machine.

Milestone 2 - task 2:
After creating the 4 different classes for the image project model, I download the model from the "Tensorflow" tab in the Teachable-Machine tool. The 2 files that are downloaded were keras_model.h5, which is a model structure and labels.txt, which is the parameters of a deep learning model. These 2 files cannot be run but will be loaded into the Python application.

Milestone 3 - task 1:
Before entering any code for this project, I had to create a conda environment by entering _conda create -n rps_, which the rps is the environment that is created in conda. After creating the rps environment, I had to activate the environment by entering _conda activate rps_ and then install pip by entering conda install pip, which the pip will be used for installing various libraries. I had to install 3 libraries, which are required for the this project and they are opencv-python, tensorflow and ipykernel. The code that i used for installing these libraries are _pip install opencv-python_, _pip install tensorflow_ and _pip install ipykernel_.

Milestone 3 - task 3:
After creating and activating the environment and installing the 3 libraries, the next document to create was the _requirements.txt_, which the command was _pip list > requirements.txt_. By creating the _requirements.txt_ file it allows other users to use my computer easily when installing these exact dependencies by running the following command: _pip install requirements.txt_

Milestone 4 - task 1:
In this Milestone 4 is where I now enter the code for the Rock Paper and Scissor game. First, I need to create a file called _manual_rps.py_, which will be used to play the game manually without the use of the camera. The import random module is required for getting the Rock, Paper and Scissors option randomly. There are 2 functions that I need to create for this game, which are _get_computer_choice_ and _get_user_choice_. get_computer_choice function will have the _random.choice_ as the computer input will be a enter randomly. Whereas the _get_user_choice_ function will have user to input their choice manually. 

So the code for the _get_computer_choice_ is as follows:

_def get_computer_choice():
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    print(f"The Computer's choice is: {computer_choice}")
    return computer_choice_
    
and the code for _get_user_choice_ is as follows:

_def get_user_choice():
    user_input = input("What is your choice? ")
    print(f"\nUser input is: {user_input}")
    return user_input_
    
Milestone 4 - task 2:
_get_winner_ function is created and passing 2 arguments in the parentheses, which are _computer_choice_ and _user_choice_

_def get_winner(computer_choice=str, user_choice=str):_

In this _get_winner_ function, it will have if-elif-else statements, which will define if whether the computer won or user won or if it's a tie in the game.

Milestone 4 - task 3:
play function is created to run the game and the code that I used to active the game is as follows:

_def play():
    user_choice = get_user_choice()     # Calls the get_user_choice function
    computer_choice = get_computer_choice()     # calls the get_computer_choice function

    return get_winner(computer_choice=computer_choice, user_choice=user_choice)     # calls the get_winner function

play()  # calls the play function and run the game

Here is a part from the game:

<img width="567" alt="2023-01-12" src="https://user-images.githubusercontent.com/119499198/212205014-526be933-7b8f-44d7-9c6c-39338772dda3.png">


_
