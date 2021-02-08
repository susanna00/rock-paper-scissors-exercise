# Rock-Paper-Scissors-exercise

The Rock Paper Scissors is an interactive game that allows a human user to play against a computer opponent. 

## 1) SETUP
# 1.1) Repository setup 
 
 Before you start with the implementation of the game you need to be sure to go through some key steps to setup your computer. 

You need to first create a new repository on Github.com and call it "rock-paper-scissors-exercise' for example. 

Remember to add the "README.md" file and a Python-flavored ".gitignore" file. 

At the end of this process you will be able to view the address of your repository on GitHub at an address such as (https://github.com/YOUR_USERNAME/rock-paper-scissors-exercise) 

Download your repository on your Desktop or another location on your computer. 

Once downloaded you will be able to navigate the repository from your command-line application: 

```sh
cd ~/Desktop/rock-paper-scissors-exercise
```

Create a new file in your repository called "game.py".This can be done either from your command-line application or directly from your text editor. 

Then, place the following contents inside your new file and always remember to save it. 

```sh
game.py
print("Rock, Paper, Scissors, Shoot!")
```


## 1.2) Environment Setup 

If you are working with environment variables and requiring a third-party package called "python-dotenv" to read the variables from the ".env" file you need to use a new project-specific Python environment where you can install the specific required packages. Hence: 

Create and activate a new project-specific Anaconda virtual environment: 

```sh
conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
```

Now, from the command-line you should be able to run the Python script: 

```sh
python game.py
```

Once you see the "Rock, Paper, Scissors, Shoot!" message, you can move forward with the implementation of the exercise. 


## 2) IMPLEMENTATION 

There are many ways to complete the implementation of the exercise. Nonetheless, to facilitate the process, I would suggest to start by adding first a welcoming message, and then proceed with each step. 

> NOTE: You should aim to make separate commits for each section. 

Thus, start with a welcoming message such as: 

```sh
Welcome 'Player One' to my Rock-Paper-Scissors game...
```

## 2.1) Ask user for an input 

The aim of this step is to ask the user to input an option between "rock", "paper", or "scissors". For this purpose use the input function: 

```sh
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': rock")

print(f"You chose: {user_choice}")
```

## 2.2) Validate User Input 

This step aims at understanding if the user has chosen a valid option, that is "rock", "paper", or "scissors", as an invalid option would cause the program to stop executing. 
First, present the valid options ("rock", "paper", "scissors").
Second, use the "if" statement function along with the [else] keyword, followed by a colon ([:]), and one indented line that contain the "INVALID" statement if a valid option has not been chosen. 
Finish by adding the [exit()] keyword after the else function to stop the program. 

'''sh 
valid_options = ["rock", "paper", "scissors"]

if user_choice in valid_options: 
    print ("VALID")
else:
    print ("INVALID")
    exit()
'''

## 2.3) Simulate Computer Selection 

The purpose of this step is to make the application randomlu select and assign the computer player's option between "rock", "paper", or "scissors". 
Use the [choice()] function to randomly select an option within the [valid_options()] list you previously created. 
Then, use the [print()] function to assign the option as the computer player's choice. 

> NOTE: It is really important to remember to add: "import random" (for convenience's sake I added it at the beginning of the exercise). This module avoids to display the message 'NameError: name 'random' is not defined'. 

Your code should look like this: 
'''sh
import random 

computer_choice = random.choice(valid_options)

print(f"The computer chose: {computer_choice}")
'''

## 2.4) Determine the winner 

This step aims at determing the winner by comparing the user's and the computer's selection. The code should include four different possibilities: 

    1. "Tie" resulting from Rock vs Rock, Paper vs Paper, and Scissors vs Scissors
    2. Rock beats Scissors 
    3. Paper beats Rock
    4. Scissors beats Paper 

For the purpose of this step use "if" statements, which are defined by the if keyword, followed by a condition to be evaluated, followed by a colon (:). The "if" statement contains [elif] keywords, also followed by a colon (:), followed by indented lines that contain the statements to be executed if the condition is met. I.e.:
    
    1."...Nobody won, it's a tie"
    2. "Congratulations! You won!! :)"
    3. "Oh, the computer won. It's ok. :("

Lastly, add an [else] keyword followed by a colon (:), followed by an indented line that contain a statement ("Oh no, something went wrong :( ") to be executed if the original condition is not met. 

Your code should look like the following, however you can adjust the statements as you wish: 

'''sh 
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
'''

## 2.5) Final information output 

Add a final friendly farewell message, such as "Thank you for playing! The game is over, please play again!". 

