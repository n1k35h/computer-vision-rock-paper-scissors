import cv2
from keras.models import load_model
import numpy as np
import random
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)   #   opens the camera
labels = open('labels.txt', 'r').readlines()
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction():
    """Ask the user to choose between "Rock", "Paper", "Scissors" as 
    an input, and returns the user's choice
    
    Arguments: None"""

    timer = 5

    while True:
        # Read and Display each frame
        ret, frame = cap.read() 
        resized_img = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_img)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)

        cv2.imshow('RPS', frame)
        print(prediction)

        # Check for key pressed        
        key = cv2.waitKey(125)

        # setting the key to start the countdown
        # if key 's' is pressed it starts the countdown
        if key == ord('s'):
            start_time = time.time()
            
            while timer >= 0:
                ret, frame = cap.read()

                # this displays the countdown number and specify the font style 
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, str(timer), (200, 250), font, 7,(0, 255, 255), 5)
                cv2.imshow('RPS', frame)
                cv2.waitKey(125)

                # current time
                current_time = time.time()

                # if time goes pass one second then reduce the count
                if current_time-start_time >= 1:
                    start_time = current_time
                    timer = timer-1

            else:
                ret, frame = cap.read()

                cv2.waitKey(2000)

                # cv2.imwrite('camera.jpg', frame)

               
        # press 'q' to quit the game or closed the video 
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # close the camera
    cap.release()

    # close the opened windows
    cv2.destroyAllWindows()

def get_computer_choice():
    computer_choice = random.choice(labels)
    print(f"The Computer's choice is: {computer_choice}")
    return computer_choice

def get_winner(computer_choice=str, user_choice=str):
    if computer_choice == "Rock" and user_choice == "Rock":
        # print("Computer chooses Rock")
        print("\nIt is a tie!")

    elif computer_choice == "Rock" and user_choice == "Scissors":
        # print("Computer choose Rock")
        print("\nYou lost")

    elif computer_choice == "Rock" and user_choice == "Paper":
        # print("Computer choose Rock")
        print("\nYou won!")
    
    elif computer_choice == "Paper" and user_choice == "Paper":
        # print("Computer chooses Paper")
        print("\nIt is a tie!")

    elif computer_choice == "Paper" and user_choice == "Scissors":
        # print("Computer choose Paper")
        print("\nYou won!")

    elif computer_choice == "Paper" and user_choice == "Rock":
        # print("Computer choose Paper")
        print("\nYou lost")

    elif computer_choice == "Scissors" and user_choice == "Scissors":
        # print("Computer chooses Scissors")
        print("\nIt is a tie!")

    elif computer_choice == "Scissors" and user_choice == "Rock":
        # print("Computer choose Scissors")
        print("\nYou won!")

    elif computer_choice == "Scissors" and user_choice == "Paper":
        # print("Computer choose Scissors")
        print("\nYou lost")
    else:
        ("\nPlease display a valid option to the Camera!")

def play():
    user_choice = get_prediction()     # Calls the get_prediction function
    computer_choice = get_computer_choice()     # calls the get_computer_choice function

    return get_winner(computer_choice=computer_choice, user_choice=user_choice)     # calls the get_winner function

play()  # calls the play function and run the game