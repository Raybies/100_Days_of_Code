import symbol


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

# User Inputs
num1 = int(input("What is the first number? "))


# To have user input math operator
for operator in operations:
    print(operator)
operator = input("Pick and operation form the line above: ")

num2 = int(input("What is the second number? "))


#!  OK so we set calculation_function to look up * and write multiply, THEN (num1, num2) are the parameters we pass through as n1, n2 in the function multiply(n1, n2)
# Make variable where the math operator is looked up to match the function names, i.e. * = multiply
calculation_function  = operations[operator]
answer = calculation_function(num1, num2) # calculation_function each have returns so the value is output

# Display results for user
print(f"{num1} {operator} {num2} = {answer}")
