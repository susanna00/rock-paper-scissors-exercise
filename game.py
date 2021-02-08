# game.py

import random 

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#
# Ask user for an input
#

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': rock")

print(f"You chose: {user_choice}")

#
# Validate user input
#

valid_options = ["rock", "paper", "scissors"]

if user_choice in valid_options: 
    print ("VALID")
else:
    print ("INVALID")
    exit()

#
# Simulate a computer input 
#

computer_choice = random.choice(valid_options)

print(f"The computer chose: {computer_choice}")

#
# Determining who won
#

computer_choice = computer_choice.lower()
user_choice = user_choice.lower()

if computer_choice == user_choice:
    print("...Nobody won, it's a tie")
elif computer_choice == "rock":
    if user_choice == "scissors":
        print ("Oh, the computer won. It's ok. :(")
    elif user_choice == "paper":
        print ("Congratulations! You won!! :)")
elif computer_choice == "scissors":
    if user_choice == "paper":
        print("Oh, the computer won. It's ok. :(")
    elif user_choice == "rock":
        print ("Congratulations! You won!! :)")
elif computer_choice == "paper":
    if user_choice == "rock":
        print ("Oh, the computer won. It's ok. :(")
    elif user_choice == "scissors":
        print ("Congratulations! You won!! :)")
else: 
    print("Oh no, something went wrong :((")


print("-------------------")
print("Thank you for playing! The game is over, please play again!")
print("-------------------")





