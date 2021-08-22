# Functions, Code Block and While Loops
# Functions: predefined code for a set of actions
# how to define custom functions use def keyword, name():
def my_function():
    # do things
    print("Hello")
    print("Bye")

# execute function aka "call function"
my_function()

def jump():
    #Do things
    print()

def turn_left():
    print()    

def move():
    print()
    
# Reeborg's World Challenge (note functions defined in the website)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Reeborg's World Jump (note functions defined in the website)
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()


