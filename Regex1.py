import re

def disemvowel(string):
	return re.sub(r'[aeiouAEIOU]',
					'',
					string)



print(disemvowel("My car is White"))

#BEST: re.sub('[aeiou]', '', string, flags = re.IGNORECASE)