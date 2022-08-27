# game_level = 3
#
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#         return new_enemy
#
# print(new_enemy)

enemies = 1

def increase_enemies():
    return enemies + 1 #returning the value without updating the variable
    print(f"enemies inside function: {enemies}")

enemies = increase_enemies() #when function is called it updates the variable enemies to be the output of the function without changing the value of the variable
print(f"enemies outside function: {enemies}")