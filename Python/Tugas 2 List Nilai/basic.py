def standard_deviasi(sequence_of_numbers):
	std = 0
	sqrt2 = 0.5
	average = rata_rata(sequence_of_numbers)
	population = count(sequence_of_numbers)
	up = 0

	for i in sequence_of_numbers:
		up += (i - average) ** 2

	std = (up / population) ** sqrt2

	return std

def rata_rata(sequence_of_numbers):
	total = 0

	for i in sequence_of_numbers:
		total += i

	average = total / count(sequence_of_numbers)

	return average

def count(sequence_of_numbers):
	count = 0

	for i in sequence_of_numbers:
		count += 1

	return count

def max_min(sequence_of_numbers):
	max = 0
	min = 100

	for i in sequence_of_numbers:
		if max < i:
			max = i

		if min > i:
			min = i

	return max, min

def modus(sequence_of_numbers):
	unique_number = unique(sequence_of_numbers)
	clist = []

	for i in unique_number:
		c = 0
		for j in sequence_of_numbers:
			if i == j:
				c += 1
		clist.append(c)

	max = 0
	index = 0

	for i in range(0, count(clist)):
		if max < clist[i]:
			max = clist[i]
			index = i

	"""
	num_count = {}

	for number in sequence_of_number:
		if number in num_count.keys():
			num_count[number] += 1
		else:
			num_count[number] = 1
	"""

	return unique_number[index]

def unique(sequence_of_numbers):
	new_sequence_of_numbers = []

	for number in sequence_of_numbers:
		if number in new_sequence_of_numbers:
			del(sequence_of_numbers[sequence_of_numbers.index(number)])
		else:
			new_sequence_of_numbers.append(number)

	return new_sequence_of_numbers