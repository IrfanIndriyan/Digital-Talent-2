def calculate_bmi(weight, height):
	"""calculate_bmi

	Calculating bmi based on weight in kg and height in m
	
	Formula:
	BMI = weight / height^2
	"""
	return weight / height ** 2


def bmi_catagories(bmi):
	"""bmi_catagories

	Find body catagories by the value of bmi
	"""

	catagory = ""

	if bmi < 15:
		catagory = "Very severely underweight"

	elif bmi >= 15 and bmi < 16:
		catagory = "Severely underweight"

	elif bmi >= 15 and bmi < 18.5:
		catagory = "Underweight"

	elif bmi >= 18.5 and bmi < 25:
		catagory = "Normal (healthy weight)"

	elif bmi >= 25 and bmi < 30:
		catagory = "Overweight"

	elif bmi >= 30 and bmi < 35:
		catagory = "Moderately obese"

	elif bmi >= 35 and bmi < 40:
		catagory = "Severely obese"

	else:
		catagory = "Very severely obese"

	return catagory