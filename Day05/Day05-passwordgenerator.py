# Password Generator

# import random module for use
import random

# Define our lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# get inputs
print("Welcome to PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password? \n"))
num_symbols = int(input("How many symbols would you like? \n"))
num_numbers = int(input("How many numbers would you like? \n"))

#### EASY LEVEL #####

# select letters
password = " "
for char in range(1, num_letters + 1):
    # add the values to the string
    password  += random.choice(letters)

# select symbols
for char in range(1, num_symbols + 1):
    # add the values to the string
    password += random.choice(symbols)

# select numbers
for char in range(1, num_numbers + 1):
    # add the values to the string
    password += random.choice(numbers)

# print easy password
print(password)

#### HARD LEVEL #####

# randomizing the variables into a list instead of a string
password_list = []
for char in range(1, num_letters + 1):
    # append the values to the list
    password_list.append(random.choice(letters)) 

# select symbols
for char in range(1, num_symbols + 1):
    # append the values to the list
    password_list.append(random.choice(symbols)) 

# select numbers
for char in range(1, num_numbers + 1):
    # append the values to the list
    password_list.append(random.choice(numbers)) 

# use shuffle to randomize the list
random.shuffle(password_list)

# convert list to string using for loop
password = ""
for char in password_list:
    password += char
print(password)