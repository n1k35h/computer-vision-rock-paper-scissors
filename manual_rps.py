import random

def get_computer_choice():
    computer_choice = random.choice(["Rock", "Paper", "Scissors", "Nothing"])
    print(f"The Computer's choice is: {computer_choice}")
    return computer_choice

def get_user_choice():
    user_input = input("What is your choice? ")
    print(f"User input is: {user_input}")
    return user_input
