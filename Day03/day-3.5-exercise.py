#Logical Operators


# if condition:
  #  do this
# else:
  #  do this

# And, both need to be true to be evaluted as true, if one is true and one is false the whole condition is evaluated as false
# Or, one or the other must be evaluted as true, then the whole condition is evaluated as true, if both are false, the whole condition is false, if both are true then the condition is evaluated as true
# Not , reverses condition logic

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?  "))
bill = 0

if height >= 120: # evaluates true or false [boolen]
    print("You can ride the rollercoaster!") # one block of code inside the if statement [true]
    age = int(input("What is your age? "))

#nested condition, which is only looked if the first condition is true
    if age < 12: 
        bill = 5
        print("Ticket is $5.")

#between 12 and 18, because the first condition checked if they were under 12, can have as many elif as you need    
    elif age <= 18: 
        bill = 7
        print("Ticket is $7.")
# between 45 and 55 years for mid-life crisis.

    elif age >= 45 and age <= 55:
        bill = 0 # don't need the bill since the bill = 0 up above
        print("Your ticket is free, you are having a mid-life crisis.")
# if first two conditions were false then
    else: 
        bill = 12
        print("Ticket is $12.")

#photo logic is nested in the hight statement
    picture = input("Do you want a photo (Y, N)? ")

#note this new if statement is nested in the original hight question
    if picture.upper() == "Y":        # note used .upper() to convert lower case input into cap to use logic
        bill += 3      # short hand of "bill = bill + 3"

# note that print is indented to large if level, but still within the original height question
    print(f"Your total is ${bill}.") 

else: 
    print("Sorry, you are too short to ride.") # block of code inside the else statement [false]