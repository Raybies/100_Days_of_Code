# Make a tip calculator
welcome = "Welcome to the tip calculator."
print(welcome)

# input for total bill and convert to float
bill = float(input("What is the total amount for the bill? $ "))
round_bill = round(bill, 2)


# input for percent tip and convert to integer
tip = int(input("What is the tip percentage you wish to leave?  "))

# convert % tip to decimal
dec_tip = (tip / 100)

# Input for how many people are spliting bill and convert to integer
people = int(input("How many people will be spliting this bill?  "))


# do math 
bill_w_tip = bill * dec_tip + bill
each_pays = bill_w_tip / people  #float
each_pays_round = round(each_pays, 2) #round to two decimal places
# alt way to do same thing as round in line above
each_pays_round = "{:.2f}".format(each_pays)

# output
message = f"For a {tip}% tip on a ${round_bill} bill, each person pays ${each_pays_round}"
print(message)