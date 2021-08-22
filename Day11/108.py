import random

################### deal() ###############################

def deal():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
############ play_game #############
def play_game():
    """Plays the Game"""
    # lists for storing drawed cards
    players_cards = []
    dealers_cards =[]

    # swtich for while loop to end game
    is_game_over = False

    # to deal cards
    for _ in range(2): #loop twice
        # appends the random choice card to the list
        players_cards.append(deal()) 
        dealers_cards.append(deal())   

    # Game playing 
    while not is_game_over:
        player_score = calc(players_cards)
        dealer_score = calc(dealers_cards)
        print(f"Your deal is {players_cards} for a total of {player_score}.")
        print(f"Dealer has {dealers_cards[0]}.")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            hit = input("Do you want to hit? [Y/N]\n").upper()
            if hit == "Y":
                players_cards.append(deal())
            else:
                is_game_over = True

    # to have dealer add new card (dealer stratagy)
    while dealer_score != 0 and dealer_score < 17:
        dealers_cards.append((deal()))
        dealer_score = calc(dealers_cards)

    # evalutes winner & prints results
    print(f"Your hand is {players_cards}.")
    print(f"Dealer has {dealers_cards}.")
    print(compare(player_score, dealer_score))     

################### calc() ###############################

# to calc
def calc(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2: # sum cards if only 2 cards drawn
        return 0 # BLACKJACK
    if 11 in cards and sum(cards) > 21:
        cards.remove(11) # remove ace value of 11
        cards.append(1) # add value of 1 in place
    return sum(cards)

################### compare() ###############################

def compare(player_score, dealer_score): # order matters, and return exits function
    if player_score == dealer_score:
        return "Draw."
    elif dealer_score == 0:
        return "You lose, dealer has Blackjack."
    elif player_score == 0:
        return "Blackjack! You win."
    elif player_score > 21:
        return "BUST! You lose."
    elif dealer_score > 21:
        return "Dealer Busts, you Win!"
    elif player_score > dealer_score:
        return "You Win!"
    else:
        return "You lose."

##### Play #######

while input("Would you like to play a game of BLACKJACK [Y/N]?").upper() == "Y":
    print("\033c") # clears screen
    play_game()