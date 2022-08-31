# year = int(input("Which year do you want to check? "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not a leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not a leap year.")

# cleaner leap year check
year = int(input("Which year do you want to check? "))

if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
    print("Leap year.")
else:
    print("Not a leap year.")
