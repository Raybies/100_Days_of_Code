# average height

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

#using python tools short version
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)


# how sum and len work long version
# sum function
total_height = 0
for hight in student_heights:
    total_height += hight
print(f"sum = {total_height}")

# lem function
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"n = {number_of_students}")

# calculate average 
average_height = total_height / number_of_students
print(f"The average height is {average_height} unit of measure.")