# love calculator
# instructions for this program: count the number of times T, R, U, E, L, O, V, E in names then use the percentage of counts of TRUELOVE/ total letters in names
print("Welcome to the Love Calculator!")

#Name inputs
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# count total letters
count_letters = len(name1) + len(name2)

# convert inputs to lowercase to use .count() for individual letters in next step and add together
names = name1.lower() + name2.lower()

# get total number of letters that are "TRUE LOVE" by counting each letter using .count()
love_letters = names.count("t") + names.count("r") + names.count("u") + names.count("e") + names.count("l") + names.count("o") + names.count("v") + names.count("e")

# score the names and convet to %
score = round((love_letters / count_letters) * 100)

# do the evaluation
# <10 and >90
if (score >= 90) or (score <= 10): # parenthsis helps make code readable
    print(f"Your score is {score}, you go together like coke and mentos!")

# between 40 and 50
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")

# else 
else:
    print(f"Your score is {score}, maybe re-evaluate your life choices.")