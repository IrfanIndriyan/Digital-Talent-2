from bmi import *

print ("""Body Mass Index (BMI)
	
Note. All input in this program are considered as weight (KG) and height (CM).
""")

weight = float(input("Weight: "))
height = float(input("Height: ")) / 100

bmi = (weight = weight, height = height)
bmi_catagory = bmi_catagories(bmi)

print ("BMI\tBMI Catagory")
print ("%.2f" % bmi, bmi_catagory, sep = '\t')