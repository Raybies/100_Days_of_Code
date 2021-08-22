# Make a heads or tails game

#import random module
import random

# define coin variable
coin = random.randint(0,1)
print(coin)
# define logic
if coin == 1:
    print("Heads")
else:
    print("Tails")

