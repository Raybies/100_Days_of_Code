# lists
# Variable where things that are realted at grouped
# Order of group

# variable = [item1, item2] 
# note that count starts at 0, not 1

fruits = ["apple", "pear", "kiwi"]
print(f"{fruits [1]}") # prints pear

states_of_america = ["null", "Delaware", "Pennsylvania", "New Jersey", "Georgia", ]
state_list = ['null', 'Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']

# enter state number
number = int(input("State number? ")) 
# print the state at that number
print(f"The {number} state entered into the Union was {state_list [number]} .") 

# states_of_america[1] = "Delawear" # using index [] you can edit field

# states_of_america.append("new variable to list at end of list") # .append() function
# states_of_america.extend(["list 1", ["list 2"]]) # .extend() function to add lots to list