# Scope:
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local scope 
    #within a function

def drink_potion():
    potion_strength = 2
    #print(potion_strength)
    print(player_health)

player_health = 10
drink_potion()
#print(potion_stregth) # cannot access outside of function drink_potion()


    