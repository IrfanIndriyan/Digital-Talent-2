import random
from basic import *

# Generate random
nilaiTugas = []
for i in range(0,250):
	nilaiTugas = nilaiTugas + [random.randrange(1,100,1)]

print (nilaiTugas)

# TAMPILKAN:
# ganjil
for i in nilaiTugas:
	if i % 2 == 1:
		print (i, end=', ')

# nilai > 70
count_70 = 0

for i in nilaiTugas:
	if i > 70:
		count_70 += 1

print (count_70)

# standar deviasi
std = standard_deviasi(nilaiTugas)
print ("Standar deviasi: ", std)

# maksimum
max, min = max_min(nilaiTugas)
print ("Max: ", max)

# minimum
print ("Min: ", min)

# modus
mode = mode_with_list(nilaiTugas)
print ("Modus(list): ", mode)
mode_dict = mode_with_dict(nilaiTugas)
print ("Modus(dict): ", mode_dict)