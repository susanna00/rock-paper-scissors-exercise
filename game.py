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



