##########
# Play Computer
# year = int(input("What's your birth year? "))
# if year >= 1980 and year < 1994:
#     print("You are a Millenial.")
# elif year >= 1994:
#     print("You are a Gen Z.")
# else:
#     print("OK Boomer!")

#########
# Fix the Errors
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at {age}.")
# else:
#     print("You can drive at 16.")

############
# Print is your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

##########
# Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])