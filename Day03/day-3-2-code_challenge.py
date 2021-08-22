# BMI Calculator
# Make vairable height and make input asking for height
height = float(input('What is your height in meters?:'))
# Make variable weight and make input asking for weight, convert variable to float to do divison math
weight = float(input('What is your weight in kg?:'))

# Make variable called bmi that contains bmi calculation of kg/m^2
bmi = weight / (height ** 2)

# Make new variable called bmi_as_int and round to one decimal point
bmi_as_int = round(bmi, 1)


# Conditional statement to categorize the BMI results.

# < 18.5 underweight
if bmi_as_int < 18.5:
    print(f"Your BMI is {bmi_as_int}, you are underweight.")

# >= 18.5 < 25 normal weight
elif bmi_as_int < 25:
    print(f"Your BMI is {bmi_as_int}, you are normal weight.")

# >=25 < 30 overweight
elif bmi_as_int < 30:
    print(f"Your BMI is {bmi_as_int}, you are overweight.")

# >= 30 < 35 obese
elif bmi_as_int < 35:
    print(f"Your BMI is {bmi_as_int}, you are obese.")

# >= 35 clinically obese
else:
    print(f"Your BMI is {bmi_as_int}, you are clinically obese.")
