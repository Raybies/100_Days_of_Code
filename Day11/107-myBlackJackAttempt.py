# Blackjack game
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#Todo 1 import random 
import random
#todo 2 make index of cards and values
# JQK = 10 and A = 1 or 11
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]

#Todo 3 make game play 1st card
# computer random, using cards for better user xp, as 123 are in order where 0 is on the other end of the keyboard
players_cards = []
dealers_cards =[]

# elif dealer_total > player_total and dealer_total < 21:
#         print("Dealer Wins")
        
#     elif player_total > dealer_total and player_total < 21:
#         print("YOU WIN!")

def deal():
    players_cards.append(random.choice(cards))
    players_cards.append(random.choice(cards))
    dealers_cards.append(random.choice(cards))
    dealers_cards.append(random.choice(cards))
    player_total = sum(players_cards)
    dealer_total = sum(dealers_cards)       
    print(f"Your deal is {players_cards} for a total of {player_total}\nDealer has [{dealers_cards[0]}, X].")
    calc_cards(player_total, dealer_total)

     

# calculate cards and display results
def calc_cards(player_total, dealer_total):
    #player_total = sum(players_cards)
    #dealer_total = sum(dealers_cards)
    if player_total == 21:
        print("BLACKJACK! You WIN.")

    elif player_total == 21 and dealer_total == 21:
        print(f"Dealer has [{dealers_cards}].")
        print("DRAW!")     

    elif player_total > 21:
        if 11 in players_cards:
            player_total = player_total - 10
            calc_cards(player_total, dealer_total)
        else:
            print(f"Dealer has [{dealers_cards}].")
            print("BUST You Lose.")  

    elif player_total < 21 and player_total < dealer_total:
        hit(player_total, dealer_total)
    
    



def hit(player_total, dealer_total):
    hit = input("Do you want to hit? [Y/N]\n").upper()
    if hit == "Y":
        players_cards.append(random.choice(cards))
        player_total = sum(players_cards)
        print(f"Your deal is {players_cards} for a total of {player_total}\nDealer has [{dealers_cards[0]}, X].")
        
        if dealer_total == 21:
            print("BLACKJACK! Dealer Wins.")
        else:
            calc_cards(player_total, dealer_total)
        #hit(player_total, dealer_total)

    elif hit == "N": 
        #calc_cards(player_total, dealer_total)
        dealer_play(player_total, dealer_total)
            

def dealer_play(player_total, dealer_total):  
    
    while dealer_total < 21:
        dealers_cards.append(random.choice(cards))
        dealer_total = sum(dealers_cards)
        print(f"Your deal is {players_cards} for a total of {player_total}\nDealer has {dealers_cards}, for a total of {dealer_total}.")
        calc_cards(player_total, dealer_total)
        #if dealer_total == 21 and player_total != 21:
            #print("Dealer has BLACKJACK. Dealer Wins!")
        
        #else:
            
            #if dealer_total > 21:
                #if 11 in dealers_cards:
                    #dealer_total = dealer_total - 10
                    #calc_cards(player_total, dealer_total)   
                
            #elif dealer_total > player_total and dealer_total < 21:
               # print("Dealer Wins!")
           #else:
                #print("Dealer BUST! You Win.")
                #print(f"Your deal is {players_cards} for a total of {player_total}\nDealer has {dealers_cards}, for a total of {dealer_total}.")





deal()

