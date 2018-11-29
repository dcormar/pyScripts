import re

def presses(string):
	regexStr = '({})'.format('|'.join([re.escape(x) for x in dict.keys()]))
	regex = re.compile (regexStr)
	return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]],string, re.IGNORECASE)
	#regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]],string)



text = "Larry Wall is the creator of Perl"

dict = {
    "Larry Wall" : "Guido van Rossum",
    "creator" : "Benevolent Dictator for Life",
    "Perl" : "Python",
}



print(presses(text))


'''	return [re.sub(r'[ ADGJMPTW]', '1', string, flags = re.IGNORECASE) \
		.sub(r'[BEHKNQUX]', '2', string, flags = re.IGNORECASE) \
		.sub(r'[CFILORVY]', '3', string, flags = re.IGNORECASE) \
		.sub(r'[SZ]', '4', string, flags = re.IGNORECASE)] \





'''
#IGUALES: print ('({})'.format('|'.join([re.escape(x) for x in dict.keys()])))  =======    print ("(%s)" % "|".join(map(re.escape, dict.keys())))
