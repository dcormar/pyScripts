import math

def find_next_square(sq):
	rootSq = math.sqrt(sq)
	return -1 if int(rootSq) != rootSq else int((rootSq+1)**2)



print(find_next_square(144))

#BEST:
'''
x = sq**0.5    
    return -1 if x % 1 else (x+1)**2
'''