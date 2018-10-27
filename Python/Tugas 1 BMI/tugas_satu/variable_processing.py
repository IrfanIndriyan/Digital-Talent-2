def convert(value):
	"""convert(value)

	convert the input value from '123 unit' converted to '123 m' or '123 kg'

	return the converted value as either int or float
	"""

	import re

	new_value = ""

	# in case there is a word in caption
	value = value.lower()

	# find out the unit
	if value.endswith("cm"):
		new_value = var_conversion(re.sub(r'[^0-9.]', '', value))
		new_value /= 100

	elif value.endswith("ft"):
		new_value = var_conversion(re.sub(r'[^0-9.]', '', value))
		new_value *= 0.3048

	elif value.endswith("inch"):
		new_value = var_conversion(re.sub(r'[^0-9.]', '', value))
		new_value *= 0.0254

	elif value.endswith("g") and not value.endswith("kg"):
		new_value = var_conversion(re.sub(r'[^0-9.]', '', value))
		new_value /= 1000

	elif value.endswith("lbs"):
		new_value = var_conversion(re.sub(r'[^0-9.]', '', value))
		new_value *= 0.453592
	else:
		# check if the input is something that is not defined
		if value.endswith('m') and not value[-2].isalpha():
			new_value = var_conversion(re.sub(r'[^0-9.]', '', value))

		elif value.endswith("kg") and not value[-3].isalpha():
			new_value = var_conversion(re.sub(r'[^0-9.]', '', value))

		elif value[-1].isnumeric():
			new_value = var_conversion(re.sub(r'[^0-9.]', '', value))

		else:
			print ("Unit doesn't supported, the value will be considered as default unit")
			new_value = var_conversion(re.sub(r'[^0-9.]', '', value))

	return new_value

def var_conversion(str):
	"""var_conversion

	converting the variable from str to either int or float according to the real value
	"""
	new_var = 0

	if '.' not in str:
		new_var = int(str)
	else:
		new_var = float(str)

	return new_var