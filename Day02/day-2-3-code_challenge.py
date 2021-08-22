# Make vairable height and make input asking for height
height = input('What is your height in meters?:')
# Make variable weight and make input asking for weight
weight = input('What is your weight in kg?:')
# Make variable called bmi that contains bmi calculation of kg/m^2
# Need to convert vairable into float to do the math
bmi = float(weight) / (float(height) ** 2)
# Make new variable called bmi_as_int and convert variable bmi from float to int
bmi_as_int = int(bmi)
# Print variable bmi_as_int
print(bmi_as_int)