# select a random int
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against the random number
def check_guess(guess, answer, turns):
    """checks the guess against the answer and returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}!")


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# Function to play game
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)
#print(f"Psst, the correct answer is {answer}")
turns = set_difficulty()
guess = 0
while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let user guess a number
    guess = int(input("Make a guess: "))

    #Track number of turns
    turns = check_guess(guess, answer, turns)
    if turns == 0:
        print("You've run out of guesses, you lose.")

    elif guess != answer:
        print("Guess again.")
# TODO make a check for not a numb?