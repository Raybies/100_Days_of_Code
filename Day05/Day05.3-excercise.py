# For Loop Range
# for number in range(a,b):
    #do something

total = 0
for number in range(1, 100 + 1): # note: does not include the b range (]
    total += number
print(total)

# adding evens
total = 0
for number in range(1-1, 100 + 1, 2): # note: for evens, need to omit the 1, as the loop starts with 1
    total += number
print(total)

#or
total = 0
for number in range(1, 100 + 1):
    if number % 2 == 0:
        total += number
print(total)

# adding odds
total = 0
for number in range(1, 100 + 1, 2): # note: for evens, need to omit the 1, as the loop starts with 1
    total += number
print(total)