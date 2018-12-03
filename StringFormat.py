import re
from functools import reduce

dict = {
      0 : ['year', 'years'],
      1 : ['month', 'months'],
      2 : ['day', 'days'],
      3 : ['hour', 'hours'],
      4 : ['minute', 'minutes'],
      5 : ['second', 'seconds']
}

def format_duration(seconds):
    if seconds == 0: return 'now'
    results = []
    text_elements = []
    differences = [12, 30, 24, 60, 60]
    for i in range(0,6):
        results.append(divmod(seconds if i == 0 else results[i-1][1],
            1 if i == 5 else reduce((lambda x, y: x * y),differences[i:])))
        if results[i][0] > 0: text_elements.append('{} {}'.format(results[i][0], dict[i][0 if results[i][0] == 1 else 1]))
    #all_but_last = 
    #last = 
    return ' and '.join([', '.join(text_elements[:-1]), text_elements[-1]]) if len(text_elements) > 1 else text_elements[0]

if __name__ == "__main__":
  print (format_duration(1232323))