dict = {
	"a" :  0,
	"b" :  1,
	"c" :  2,
	"d" :  3,
	"e" :  4,
	"f" :  5,
	"g" :  6,
	"h" :  7,
	"i" :  8,
	"j" :  9,
	"k" : 10,
	"l" : 11,
	"m" : 12,
	"n" : 13,
	"o" : 14,
	"p" : 15,
	"q" : 16,
	"r" : 17,
	"s" : 18,
	"t" : 19,
	"u" : 20,
	"v" : 21,
	"w" : 22,
	"x" : 23,
	"y" : 24,
	"z" : 25
}

import re
import string

def rot13(string):
	characters = list(sorted(dict.keys()))
	ciphered = ''
	for x in string:
		replacement = characters[(dict[x.lower()] + 13) % 26] if re.match('[a-z]', x, re.IGNORECASE) else x
		ciphered += replacement if x.islower() else replacement.upper()
	return ciphered 




print(rot13("Test"))