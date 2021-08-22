import symbol
from tkinter import E


logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
# Calculator Functions

# Add 
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Power
def power(n1, n2):
    return n1 ** n2 

# Square
def square(n1, n2):
    return n1 ** (1 / n1)

# Dictionary for symbols to lookup function names
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
}


def calculator():
    #recursion, no inputs and no outputs
    print(logo)
    num1 = float(input("What is the first number? "))
    for operator in operations:
        print(operator)
    should_continue = True
    while should_continue:
        operator = input("Pick and operation form the line above: ")
        num2 = float(input("What is the next number? "))
        calculation_function  = operations[operator]
        answer = calculation_function(num1, num2) 

        print(f"{num1} {operator} {num2} = {answer}")
        
        if input("Do you want to add another operation? [Y/N]").upper() == "Y":
            num1 = answer
        else:
            should_continue = False
            calculator() # start at the beginning - reset
    
      
calculator()
