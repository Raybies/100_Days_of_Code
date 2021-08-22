# conditional statements
#if condition:
#    do this (if true)  #indentation is important in python
#else:
#    do this (if false)

#water_level = 50 #water level of bathtub
#if water_level > 80:
   # print("Drain Water")
#else: #else and if need to be at same indent level
    #print("Rubber Ducky")

# Ticket Box
# must be >120 cm to get ticket
# draw.io (web app for flow chart building)

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?  "))

if height >= 120: # evaluates true or false [boolen]
    print("You can ride the rollercoaster!") # one block of code inside the if statement [true]
else: 
    print("Sorry, you are too short to ride.") # block of code inside the else statement [false]

#Comparison Operators
    # > greater than
    # < less than
    #  >= greater than or equal to
    # <= less than or equal to
    # == equal to
    # != not equal to
    # % modular 7 % 2, gives remander [3 remander of 1]