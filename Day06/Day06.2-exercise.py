# Indentation
# Things indented is "in" the code block 
# Indentation is 4 spaces
# For Loop, run through sequence
# While Loop, when condition is true, continue loop, when condition is false then exit loop

def jump():
    #Do things
    print()

number_of_hurdles = 6

while number_of_hurdles > 0:
    jump() #action
    number_of_hurdles -= 1 # counter
    print(number_of_hurdles)
    # when the number_of_hurdles = 0, code block is exited

at_goal = 0

while at_goal != True:  # when not equal to goal is true
    jump()

while not at_goal: # while not at_goal, jump--if at at_goal, then stop
    jump()

# For Loops is good for when you want to iterate through each thing in list or a range of a list
# While loop is good for when you want to do something that is conditional, con: if will continue as an infinate loop if false or true never occurs 

# CODE CHALLENGE
# Reeborg's World (Hurdle #3)

def front_is_clear():
    print()

def wall_in_front():
    print()

def move():
    print()

while not at_goal:
    if wall_in_front():
        jump()
    else:
        move()
    
# CODE CHALLENGE
# Reeborg's World (Hurdle #4)
def turn_left():
    print()  

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def wall_on_right():
    print()

# redefine jump for 
def jump():
    turn_left()
    while wall_on_right():
        move()
    
    #exit while
    turn_right()
    move()
    turn_right()

    #new while
    while front_is_clear():
        move()
        turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# MAZE Challenge
# Follow right edge, turn right, if no right, go straight if no straight go left
def right_is_clear():
    print()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

    