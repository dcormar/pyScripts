def squaredArrays(a1, a2):
	return False if a1 is None else False if a2 is None else sorted([x**2 for x in a1]) == sorted (a2)

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(squaredArrays(a1, a2))

'''
	try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False
'''