def multiplication_table(row,col):
    matrix1 = []
    for i in range(1,row + 1):
        matrix1.append(list(range(i, (col+1)*i, i)))
    return matrix1




print (multiplication_table(3,3))

'''
Python's range() vs xrange() Functions:

You may have heard of a function known as xrange(). This is a function that is present in Python 2.x, however it was renamed to range() in Python 3.x, and the original range() function was deprecated in Python 3.x. So what's the difference? Well, in Python 2.x range() produced a list, and xrange() returned an iterator - a sequence object.
'''

#BEST: return [[(i+1)*(j+1) for j in range(col)] for i in range(row)]