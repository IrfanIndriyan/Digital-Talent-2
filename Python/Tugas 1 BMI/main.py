from variable_processing import convert
from bmi import *

print ("""Body Mass Index (BMI)

Note. the default input for weight is kg and height m
      please specify your value if it's not in kg or m

* Supported unit:
    Weight (g and lbs)
    height (cm, inch, and ft)
		
Example:
    15 lbs or 15lbs
    7 km or 7km
	""")

weight = input("Weight? ")
height = input("Height? ")

weight = convert(weight)
height = convert(height)

bmi = calculate_bmi(weight, height)
bmi_catagory = bmi_catagories(bmi)

print ("\nBMI\tBMI Catagory")
print (round(bmi, 2), bmi_catagory)

