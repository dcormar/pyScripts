def summation(num):
	return reduce((lambda x, y: x + y),range(num+1))



print(summation(20))

#BEST: return (1+num) * num / 2
#SECOND: return sum(xrange(num + 1))