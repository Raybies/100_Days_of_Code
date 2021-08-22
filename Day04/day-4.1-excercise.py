# Randomization and lists
# Merersan Twister

# import random module
import random

# modules what are they? 
# splits large code up into functional areas, useful for colaboration 
# look-up/link using import
# link to model by using model.function

# ramdon int
random_int = random.randint(1,5)
print(random_int)

# random float
random_float = random.random() # [0,1) range/doamin
print(random_float)

# random float
random_float = random.random() * 5 # [0,5) range/doamin
print(random_float)

# random float
random_float = random.random() # [0,1) range/doamin
print(random_float * random_int)

# random love score from day 3
love_score = random.randint(1, 100)
print(f"You are {love_score}% capatable.")