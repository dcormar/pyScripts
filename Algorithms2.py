from math import modf, sqrt
#THIS ONLY IN PYTHON 3: 
from functools import reduce

def getFactors(number):
  return set(reduce(list.__add__, 
                ([i, number//i] for i in range(1, int(number**0.5) + 1) if number % i == 0)))

def list_squared(m,n):
  squared = []
  for number in range(m,n+1):
    factors = list(getFactors(number))
    squaredFactorsSummatory = reduce(lambda x,y: x+y, map(lambda x: x*x, factors))
    if modf(sqrt(squaredFactorsSummatory))[0] == 0:
      squared.append([number, squaredFactorsSummatory])
  return squared

print (list_squared(1, 250))


def prueba(number):
  return list([i, number//i] for i in range(1, int(number**0.5) + 1) if number % i == 0)

#print (prueba (250))
'''
turn [[1, 2, 3], [4, 5], [6, 7, 8]] into [1, 2, 3, 4, 5, 6, 7, 8].

reduce(list.__add__, [[1, 2, 3], [4, 5], [6, 7, 8]], [])
'''


#filter(P, S) is almost always written clearer as [x for x in S if P(x)]
#map(F, S) which becomes [F(x) for x in S]

