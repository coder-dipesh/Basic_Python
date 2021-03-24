
"""Solve each of the following problems using Python Scripts. Make sure you use appropriate variable names and comments. When there is a final answer have Python print it to the screen.
A person’s body mass index(BMI) is defined as: 
BMI = mass in kg / (height in m)2.
"""
# Raw data collected
person_mass = float(input("Enter your mass in kg : "))
person_height = float(input("Enter your heignt in meter : "))

# Process
body_mass_index = person_mass/(person_height)**2

print(f'Person BMI is {body_mass_index} kg/m2')
