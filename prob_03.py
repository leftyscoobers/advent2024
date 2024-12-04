import re

input_file = 'input_03.txt'
raw_data = open(input_file, 'r').readlines()

# Extract all examples of mul(number,number) from the long string of junk
sum_of_products = 0
def mult_values(mult_string):
	x, y = [int(s) for s in re.findall(r"\d+", mult_string)]
	return x * y
	
	
for line in raw_data:
	mult_sets = re.findall(r"mul\(\d+,\d+\)", line)
	products = [mult_values(s) for s in mult_sets]
	sum_of_products += sum(products)

print(f'Part 1: Sum of multiplied pairs is {sum_of_products}') 

# do() enables fulture mul instructions and don't() disables said functions - basically toggle the mult on and off. 
pattern_w_dos = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
sum_of_products_p2 = 0
for line in raw_data[:1]:
	mults_and_toggles = re.findall(pattern_w_dos, line)
	do = True
	for s in mults_and_toggles[:50]:
		print(s)
		if s == "do()":
			do = True
		elif s == "don't()":
			do = False
		print(do)
		if 'mul' in s and do:
			sum_of_products_p2 += mult_values(s)
		print(sum_of_products_p2)

print(f'Part 2: Sum of products with do/dont toggle is {sum_of_products_p2}') # 87020895 too high

