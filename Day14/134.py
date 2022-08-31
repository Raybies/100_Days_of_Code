# Higher Lower
#TODO random pick game_data
import random
from random import randint
from 134game_data import data
# pick a random number coorisponding to an index number in data[]
pick1 = randint(0, 49)
pick2 = randint(0, 49)
print(random.choice(data))

#pull display data about the random person in data

#print(data.name[pick1])