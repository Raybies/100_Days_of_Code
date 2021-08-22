print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?  "))


if height >= 120: # evaluates true or false [boolen]
    print("You can ride the rollercoaster!") # one block of code inside the if statement [true]
    age = int(input("What is your age? "))
    if age < 12: #nested condition, which is only looked if the first condition is true
        print("Please pay $5.")
    elif age <= 18: #between 12 and 18, because the first condition checked if they were under 12, can have as many elif as you need
        print("Please pay $7.")
    else: # if first two conditions were false then
        print("Please pay $12.")
else: 
    print("Sorry, you are too short to ride.") # block of code inside the else statement [false]

