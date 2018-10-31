def standard_deviasi(sequence_of_numbers):
	"""
	"""
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
	"""
	"""
	total = 0

	for i in sequence_of_numbers:
		total += i

	average = total / count(sequence_of_numbers)

	return average

def count(sequence_of_numbers):
	"""
	"""
	count = 0

	for i in sequence_of_numbers:
		count += 1

	return count

def max_min(sequence_of_numbers):
	"""
	"""
	max = 0
	min = 100

	for i in sequence_of_numbers:
		if max < i:
			max = i

		if min > i:
			min = i

	return max, min

def mode_with_list(sequence_of_numbers):
	"""
	"""
	unique_number = unique(sequence_of_numbers)
	clist = []

	for i in unique_number:
		c = 0
		for j in sequence_of_numbers:
			if j == i:
				c += 1
		clist = clist + [c]

	max = 0
	index = 0

	for i in indexing(0, count(clist)):
		if max < clist[i]:
			max = clist[i]
			index = i

	return unique_number[index]

def mode_with_dict(sequence_of_numbers):
	"""
	"""
	num_count = {}

	for number in sequence_of_numbers:
		if number in num_count:
			num_count[number] += 1
		else:
			num_count[number] = 1

	max = 0
	key = 0

	for i in num_count:
		if max < num_count[i]:
			max = num_count[i]
			key = i

	return key

def unique(sequence_of_numbers):
	"""
	"""
	new_sequence_of_numbers = []

	for number in sequence_of_numbers:
		if number in new_sequence_of_numbers:
			# del(sequence_of_numbers[sequence_of_numbers.index(number)])
			number_index = find_index(number, sequence_of_numbers)
			sequence_of_numbers = sequence_of_numbers[:number_index] + sequence_of_numbers[number_index + 1:]
		else:
			new_sequence_of_numbers = new_sequence_of_numbers + [number]

	return new_sequence_of_numbers

def find_index(number, sequence_of_numbers):
	"""
	"""
	index = 0

	for i in indexing(0, count(sequence_of_numbers)):
		if sequence_of_numbers[i] == number:
			index = i
			break

	return index

def indexing(start, end):
	"""
	"""
	index = []
	number = start

	while number < end:
		index += [number]
		number += 1

	return index