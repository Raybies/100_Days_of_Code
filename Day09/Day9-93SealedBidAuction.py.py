# Sealed-bid Auction App



logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

#Dictionary
bids = {}

#Define function to find winning bid
def winning_bid(bidding_record):
    #{Bidder:Bid, Bidder:Bid}
    highest_bid = 0
    for bidder in bidding_record: #loops through each KEYS
        bid_amount = bidding_record[bidder] # get value #! note that this passes the dictionary and the [key] but outputs the value
        if bid_amount > highest_bid: #If the current round of looping the value is greater than the highest_bid, over write the highest_bid with new value
            highest_bid = bid_amount #set the highest value
            winner = bidder #set the key name of the highest to winner
    print(f"The winner is {winner} with a bid of${highest_bid}.")

#Start of program for User
print(logo)
print("Welcome to the Silent Auction!")

#Set variable bid_open to allow for multiple users and then exit program
bid_open = True
while bid_open:
    #Inputs
    bidder_name = input("Enter Bidder's Name: \n")
    bid_price = int(input("What is your bid? \n $"))
    bids[bidder_name] = bid_price #!need more info on why this - bids{} from above [key] of bidder_name and = value of bid_price
           
    #clear inputs so next user can't see previous bidder's bid
    print("\033c")
    
    #To exit program and display winning bid
    restart = input("Do you want to place a bid? (Y/N)? \n").upper()
    if restart == "N":
        #find winning bid
        bid_open = False #flip variable
        winning_bid(bids)
