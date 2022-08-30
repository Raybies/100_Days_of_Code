i = 0
def my_function():
    for i in range(0, 20):
        i += 1
        if i == 20:
            print("You got it!")
        else:
            print("You didn't get it.")
my_function()

from random import randint
dice_img = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5)
print(dice_img[dice_num])