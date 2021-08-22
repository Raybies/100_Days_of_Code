# Highest Score Exercise

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# max() finds max, min()--short cuts

# set new variable highest_score equal to the first value in the list
highest_score = student_scores[0]
# use for function to go through the list
for score in student_scores:
    # evaluate each n list value in order against the highest_score
    if score > highest_score:
        # if the n value is higher than the highest_score at that time, the n value becomes the next highest_score to then be evaluated against the next number in the list
        highest_score = score

# print the highest_score        
print(f"The highest score in class is: {highest_score}.")
