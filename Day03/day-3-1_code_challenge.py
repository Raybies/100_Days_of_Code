number = int(input("Which number do you want to check if its odd or even?  "))
check_number = number % 2
if check_number == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")