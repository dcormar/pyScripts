from functools import reduce

def getFactors(number):
  return set(reduce(list.__add__, 
                ([i, number//i] for i in range(1, int(number**0.5) + 1) if number % i == 0)))

def proper_fractions(n):
	proper_numerators = []
	divisors_denominator = list(getFactors(n))
	for i in range(1, int(n**0.5) + 1):
		proper = True
		for j in divisors_denominator[1:]:
			if i%j == 0:
				proper = False
				break
		if proper == True: proper_numerators.append(i)

	return len(proper_numerators).append(range(int(n**0.5) + 1,n))






print (proper_fractions(173453939393939399393939393939393))