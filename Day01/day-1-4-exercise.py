#variables, to declare a variable in python non-keyword then equal and the stored variable
# name = input("What is your name?")
# print("Hi," + name)

name = "Jack"
print(name)
name = "Angela"
print(name)


name = input("What is your name?")
length = len(name)
print(length)

#Challenge:
####################################
a = input("a: ")
b = input("b: ")
####################################
#Write your code below this line 

c = a
d = b
a = d
b = c

#SOLUTION (NOTE: writing out algorithm before code)
#put contents of variable a into new variable c, saved to move later
c = a
#put contents of variable b into existing variable a
a = b
#put contents of variable c (old a) into b
b = c

#Write your code above this line 
####################################
print("a: " + a)
print("b: " + b)