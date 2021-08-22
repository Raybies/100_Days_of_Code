# Leap year 
year = int(input("Which year do you want to check?  "))

# figure out if a leap year
# Evenly divisable /4 is leap, but not if /100 again, unless its /400

if year % 4 == 0:
    print("This is a leap year.")
    if year % 100 == 0 and year % 400 == 0:
        print("This is a leap year.")
else:
    print("This is not a leap year.")

# Took me less than 2 min to complete