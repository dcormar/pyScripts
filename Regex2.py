import re
from functools import reduce

def presses(phrase):
    phraseText = phrase if type(phrase) is str else str(phrase)
    return int(reduce((lambda x, y: int(x) + int(y)), [x for x in re.sub(r'[SZ]', '4', 
            re.sub(r'[CFILORVY]', '3', 
                re.sub(r'[0BEHKNQUX]', '2', 
                    re.sub(r'[ ADGJMPTW\*#]', '1', re.sub(r'[79]', '5',re.sub(r'[234568]', '4',phraseText)), flags = re.IGNORECASE), flags = re.IGNORECASE), flags = re.IGNORECASE), flags = re.IGNORECASE)]))


print(type(presses(0)))


''' 
BEST:

BUTTONS = [ '1',   'abc2',  'def3',
          'ghi4',  'jkl5',  'mno6',
          'pqrs7', 'tuv8', 'wxyz9',
            '*',   ' 0',    '#'   ]
def presses(phrase):
    return sum(1 + button.find(c) for c in phrase.lower() for button in BUTTONS if c in button)


-------
ANOTHER ONE WITH DICTS:

keys = ['1',
        'ABC2',
        'DEF3',
        'GHI4',
        'JKL5',
        'MNO6',
        'PQRS7',
        'TUV8',
        'WXYZ9',
        ' 0']


def create_dict(keys):
    letters = {}
    for key in keys:
        for i, letter in enumerate(key):
            letters[letter] = i+1
    return letters


def presses(phrase):
    presses_dict = create_dict(keys)
    return sum(presses_dict[a] for a in phrase.upper())





'''
#IGUALES: print ('({})'.format('|'.join([re.escape(x) for x in dict.keys()])))  =======    print ("(%s)" % "|".join(map(re.escape, dict.keys())))
