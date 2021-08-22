print(int(8 / 3)) # convert to int goes to decimal point
print(round(8 / 3)) # rounds to whole number
print(round(8 / 3 , 2)) # rounds to whole number with decimal place [2]
print(2.666666, 2) # 2.67
print(8 // 3) # Floor Division auto converts to int
print(type(8 // 3)) # int
print(type(8 / 3)) # float

result = 4 / 2
print(result)
result /=2 # continued math
print(result)

# Score Example
score = 0
height = 1.8
isWinning = True
# User scores a point

score += 1 # +=, -+, *=, /= other options
print(score)

# F-strings
print("Your score is " + str(score)) 
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}" ) # note f must be in front of " " and then in {} for the variable of differnt type