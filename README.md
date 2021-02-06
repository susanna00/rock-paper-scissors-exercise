# Rock-Paper-Scissors-exercise

The Rock-Paper-Scissors is an interactive game that allows a human user to play against a computer opponent. 

## 1) SETUP
## 1.1) Repository setup 
 
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

## 2.1) Asking user for an input 

The aim of this step is to ask the user to input an option between "rock", "paper", or "scissors". For this purpose use the input function: 

```sh
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': rock")

print(f"You chose: {user_choice}")
```

# 2.2) Validate