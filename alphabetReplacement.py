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

def alphabet_position(text):
	all_positions = ""
	for c in text:
		all_positions+=" " if all_positions != "" else ""
		try:
			all_positions+=str(dict[c.lower()]+1)
		except KeyError: all_positions=all_positions[:-1]
	return all_positions

print(alphabet_position("The sunset sets at twelve o' clock."))
assert (alphabet_position("The sunset sets at twelve o' clock.")=="20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")

'''
GOOD TO USE A SINGLE STRING, PLUS METHOD "INDEX", INSTEAD OF A DICTIONARY

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')
'''

'''
GOOD TO USE "ISALPHA", AND ASCII_LOWERCASE (remember to type "from string import ascii_lowercase")

return ' '.join(str(ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())