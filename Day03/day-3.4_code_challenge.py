# Pizza order program

#size, Pep, extra cheese
#Size S 15, M 20, L 25
#Pep S +2, Pep ML +3
#Cheese +1

# starting bill amount
bill = 0

# get pizza size
size = input("Welcome to Pizza Place, what size pizza do you want (S, M, L)? ")

# get pepperoni
pep = input("Do you want pepperoni on that (Y, N)? ")

# get cheese
cheese = input("Do you want extra cheese (Y, N)? ")

# Calculate Bill for Small Pizza
if size.upper() == "S":
    bill += 15 #price of small pizza 
    
    if pep.upper() == "Y":
        bill += 2 # add peperoni
    
   # don't need the else statements for this to work
    
    if cheese.upper() == "Y":
        bill += 1
    
# for Medium
elif size.upper() == "M":
    bill += 20

    if pep.upper() == "Y":
        bill += 3
        
    if cheese.upper() == "Y":
        bill += 1
    

# for large
else:
    bill += 25

    if pep.upper() == "Y":
        bill += 3
        
    if cheese.upper() == "Y":
        bill += 1
    

# Print total
print(f"Your total today is ${bill}.")

