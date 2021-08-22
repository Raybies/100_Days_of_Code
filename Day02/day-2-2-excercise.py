num_char = len(input("What is your name?"))

#if you use num_char you get get TypeError: can only concatenate str (not "int") to str
# print("Your name has " + num_char + " characters.")

#type check
print(type(num_char))
# convert int to string and put into new variable
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

#type casting (changing) new variable called new_numb_char where we use str() to convert the variable num_char from int into string
new_num_char = str(num_char)

# variable a is a int
a = 123
print(type(a))

# variable a is a string
a = str(123)
print(type(a))

#convert string 100.5 to convert into type float to convert to 100.5 as float
print(70 + float("100.5"))