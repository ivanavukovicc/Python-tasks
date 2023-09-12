numbers = []

for n in range(1000, 3001):
	if n % 9 == 0 and n % 5 != 0:
		numbers.append(n)

print_numbers = ', '.join(map(str, numbers))
print(print_numbers)
