# Treasure Island choose your own adventure game

# Introduction to Game

print("Welcome to treasure island! \n")
print("Your mission is to find the treasure! \n")
quest = input("Do you accept this quest? [Y/N] ")

if quest.upper() == "Y":
    print("You are at a cross road. \nWhere do you want to go?")
    cross_road = input("Left or Right? [Left/Right]")

    # if left is chosen
    if cross_road.lower() == "left":
        print("You have come to a lake. There is an island in the middle of the lake.")
        lake = input("Type 'wait' to wait for a boat or type 'swim' to swim across the lake. [Wait/Swim] ")
    
        # if wait is chosen
        if lake.lower() == "wait":
            print("Your boat has arrived, you take the boat to the island and arrive unharmed.")
            print("On the island you find a house with three doors: one red, one blue, and one yellow.")
            door = input("What color do you choose? [Red/Blue/Yellow] ")

            # if blue is chosen
            if door.lower() == "blue":
                print("You open the door to find it full of angry beasts, the beast maul you to death!")
                print("You are dead. Game Over.")

            # if red is chosen
            elif door.lower() == "red":
                print("You find that the owner is home, more importantly, you find that the owner is an Ogar who works the night shift. You have awaken the Ogar and he's not happy.")
                print("The angry Ogar bludgens you to death.")
                print("Game Over.")

            # if yellow is chosen
            elif door.lower() == "yellow":
                print("Congratulations!! You have found the treasure!")
                print("You Win!")
            
            # if a value other than red, blue, or yellow is entered
            else:
                print("You can't follow instructions.")
                print("You are dead! Game Over.")
        
        # if swim is chosen
        elif lake.lower() == "swim":
            print("You have chosen to swim across the lake.")
            print("You forgot that you can't swim and have drowned in the icy waters.")
            print("Game Over.")
        
        # if an invalid input for lake
        else:
            print("You can't follow instructions.")
            print("You are dead! Game Over.")
    
    # if right is chosen       
    elif cross_road.lower() == "right":
        print("You find yourself at a tavern, you get caught in a bar fight and get stabed. Your quest has ended. \nGame Over.")
    
    # if value other than left/tight
    else:
       print("INVALID")
       print("You can't follow instructions.")
       print("You are dead! Game Over.")

# if no or invalid response is given
else:
    print("You have chosen not to take this quest, enjoy your simple life void of adventure.")
