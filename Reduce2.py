def row_sum_odd_numbers(n):
	previousNumbers = ((n-1)*n)/2
	return reduce((lambda x, y: x + y),map(lambda x: (2*x)+1, range(previousNumbers,previousNumbers+n)))

print (row_sum_odd_numbers(41))

#BEST: n ** 3