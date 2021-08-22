# Create a program that tells how many days weeks and months left if user lives to 90 years old
# Create variable called age where user inputs their current age
age = input("What is your current age?")
# Take users input current age and subtract it from 90 to get remaning years
time_left = 90 - int(age)

# 365 days / year
days = time_left * 365
# 52 weeks / year
weeks = time_left * 52
# 12 months / year
months = time_left * 12

# Print results
message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)