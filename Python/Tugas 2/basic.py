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

def insertion_sort(sequence_of_numbers):
	for i in xrange(1, len(sequence_of_numbers)):
		key = sequence_of_numbers[i]

		j = i - 1

		while  j >= 0 and sequence_of_numbers[j] > key:
			sequence_of_numbers[j + 1] = sequence_of_numbers[j]
			j = j - 1

		sequence_of_numbers[j + 1] = key

	return sequence_of_numbers

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
	unique = list(set(sequence_of_numbers))
	clist = []

	for i in unique:
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

	return unique[index]