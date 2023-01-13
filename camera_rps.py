import cv2
from keras.models import load_model
import numpy as np
import random

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction():
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)

        cv2.imshow('frame', frame)

        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def get_computer_choice():
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
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
    user_choice = get_prediction()     # Calls the get_user_choice function
    computer_choice = get_computer_choice()     # calls the get_computer_choice function

    return get_winner(computer_choice=computer_choice, user_choice=user_choice)     # calls the get_winner function

play()  # calls the play function and run the game
