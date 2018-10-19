from bmi import *

print ("""Body Mass Index (BMI)
	
Note. All input in this program are considered as weight (KG) and height (CM).
""")

weight = float(input("Weight: "))
height = float(input("Height: ")) / 100

bmi = calculate_bmi(weight, height)
bmi_catagory = bmi_catagories(bmi)

print ("\nBMI\tBMI Catagory")
print ("%.2f" % bmi, bmi_catagory, sep = '\t')