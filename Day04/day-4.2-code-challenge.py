# instructions: get list of names, assign random number to pull the index number in the list names

# import random module
import random

#players = ["Angela", "Ben", "Jenny", "Michael", "Chole"]

names_string = input("Give me everybody's names, separated by a comma.  ")

# Spilt string by designated divider--here its , comma
names = names_string.split(", ")

# find number of players for right end of domain for random list
number_of_players = int(len(names))

# random
draw = random.randint(0, number_of_players - 1) # note since lists start at 0, need to minus 1 to get end of domain

# make new variable set to list of name, but using variable draw (our random variable) to pick the index value
person_paying = names[draw]  

# print the name from the person_paying variable
print(f"Looks like {person_paying} is paying today!")

# using random.choice(list) this is short hand method for doing the above from number_of_players down to the print function)
person_paying1 = random.choice(names)
print(person_paying1 + " is paying today! Sucka!")


