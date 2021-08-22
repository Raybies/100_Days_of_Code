# Rock Paper Scissors

# import random
import random

# art
# variable rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# variable paper
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
# variable scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# start
throw = int(input("What do you choose? Type 1 for Rock, 2 for Paper, or 3 for Scissors. \n"))

# computer random, using 1-3 for better user xp, as 123 are in order where 0 is on the other end of the keyboard
computer_throw = random.randint(1,3)
# make the art a list and use inputs as indices
art = [rock, paper, scissors]

if throw >=4 or throw <= 0:
    print("Hey, dummy! Read the instructions!")
else:
    print(art[throw-1])
    print("The computer threw:")
    print(art[computer_throw-1])

# throw logic
# if throw == 1:
#     print(rock)
# elif throw == 2:
#     print(paper)
# else:
#     print(scissors)


# print("The computer threw:")

# # computer's throw
# if computer_throw == 1:
#     print(rock)
# elif computer_throw == 2:
#     print(paper)
# else:
#     print(scissors)

# results
    # rock 1, paper 2, scissor 3


    if throw == computer_throw:
        print("Tie.")
    elif throw == 1 and computer_throw == 2:
        print("Paper beats Rock, you lose.")
    elif throw == 1 and computer_throw == 3:
        print("Rock beats Scissors, you win.")
    elif throw == 2 and computer_throw == 1:
        print("Paper beats Rock, you win.")
    elif throw == 2 and computer_throw == 3:
        print("Scissors cuts paper, you lose.")
    elif throw == 3 and computer_throw == 1:
        print("Rock breaks Scissors, you lose.")
    elif throw == 3 and computer_throw == 2:
        print("Scissor cuts paper, you win.")
    else:
        print("You entered in an invalid number, you lose.")







