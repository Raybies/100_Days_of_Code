# Hangman

# import models
import random
from replit import clear

# word list
from hangman_words import word_list

# ASCII Art for Hangman
from hangman_art import logo, stages

# Intro Design
print(logo)

# Define word list & initial variables
# choose a random word from wordlist
chosen_word = random.choice(word_list).upper()

# Find number of letters in word
word_length = len(chosen_word)
number_of_letters = int(len(chosen_word))

# Set begining game 
end_of_game = False
lives = 6

# My solution
#hidden_word = ["_"]
#hidden_word.extend(["_"] * (number_of_letters - 1))
#print(hidden_word)

# Course solution
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter:  ").upper()
    clear()

    if guess in display:
        print(f"You've already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
          display[position] = letter     

    if guess not in chosen_word:
      lives -= 1 
      print(f"Your guess of {guess} is not in the word.")
      print(f"You have {lives} left.")
      if lives == 0:
        end_of_game = True
        print("You Lose.")
        print(f"The word was " + chosen_word)

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])



# TO DOs
# ToDo - Randomly choose a word from the word_list and assign it to a variable called chosen_word
# ToDo - Create empty list called display
# ToDo - for each letter in the chosen_word, add an "_" to the hidden_word/display apple (5) would look like 
#   ["_", "_", "_", "_", "_"]
# ToDo - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# ToDo - Add guesses, repeating Use a while loop to let the user guess again. The loop should only stop once the user 
#   has guessed all the letters in the chosen_word and 'display has no more blanks "_". 
#   Then you can tell the user they've won.
# ToDo - Create variable lives, set equal to 6
# ToDo - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
# ToDo - Loop through each position in the chosen_word
    # If the letter at that position matches guess then reveal that letter in the display 
    # ToDo - Check if the letter the use guessed (var guess) is one of the letters in chosen_word
    #for letter in chosen_word:
        #if guess == letter:
        #  print(letter)
        #else:
        # print("nope")
# ToDo - replace _ with the letter

  