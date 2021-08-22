# Dictionaries
# Module 1
# KEY => VALUE
    # {key: Value} = {"bug": "An error in a program that.."}

programming_dictionary = {
    "bug": "An error in a program that..", 
    "function" : "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["bug"])

# Add new entry to dictionary 
programming_dictionary["Loop"] = " The action of doing something over and over again."
print(programming_dictionary)

# blank dictionary
empty_dictionary = {}

# wipe an existing value = {} like game scores
#programming_dictionary = {}

print(programming_dictionary)

# overwrite an entry
programming_dictionary["bug"] = "moth is a bug, one that I think is under appreciated"
print(programming_dictionary)

# loop, only returns the key
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
