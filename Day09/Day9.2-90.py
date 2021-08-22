student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

# Todo convert number to grade 91-100 outstanding, 81-90 Exceeds Expectations, 71-80 Acceptable, 70 & lower Fail
# Todo new dictionary for the grades

student_grades = {
    
}
# Todo write code to add grades to student_grades dictionary
for student in student_scores: # to loop through all entries in dictionary #! student is the "Key"
    score = student_scores[student] # variable that the student:score #! Using student_scores[student (i.e. key)] we actually call the value {key:value}, and we are just setting it to a variable
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


print(student_grades)