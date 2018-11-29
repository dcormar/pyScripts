def add_binary(a, b):
	binary = ''
	quotient = long(a+b)
	while True:
		if quotient == 0: return binary
		elif quotient % 2 == 1 : 
			quotient = (quotient - 1)/2
			binary = '1' + binary
		else: 
			quotient = quotient/2
			binary = '0' + binary

		#ESTO DIO PROBLEMAS DE PRECISION DE LAS VARIABLES
		#quotient = float(quotient)/2
		#print ('quotient: ' + str(quotient))
		#print ('int(quotient): ' + str(int(quotient)))
		#binary = '0' + binary if quotient == long(quotient) else '1' + binary
		#quotient = long(quotient)
		#if quotient  == 0: return binary



print(add_binary(51,12))
print (1/2)

#BEST:
#return bin(a+b)[2:]
# O
#return '{0:b}'.format(a + b)

#BEST 2:
''' 
def add_binary(a,b):
    return convert_to_binary(a + b)[::-1]

def convert_to_binary(num):
    if num == 0:
        return '1'
    elif num == 1:
        return '1'
    elif num % 2 == 0:
        return '0' + convert_to_binary(num / 2)
    else:
        return '1' + convert_to_binary(num - 1)[1:]
'''