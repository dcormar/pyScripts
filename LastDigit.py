'''def last_digit(n1, n2):
    if n2 == 0:
        return 1
    cycle = [n1 % 10]
    while True:
        nxt = (cycle[-1] * n1) % 10
        if nxt == cycle[0]:
            break
        cycle.append(nxt)
    return cycle[(n2 - 1) % len(cycle)]
'''
def last_digit_matrix(matrix):
    matrix.reverse()
    print (matrix)
    first = matrix.pop()
    second=matrix.pop()
    partial_last_digit = last_digit(first, second)
    print (partial_last_digit)
    for i in reversed(matrix):
        partial_last_digit = last_digit(partial_last_digit,i)
    return partial_last_digit


def last_digit_pow(n1, n2):
    return pow(n1, n2, 10)




rules = {
    0: [0,0,0,0],   
    1: [1,1,1,1],
    2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4,6,4,6], 
    5: [5,5,5,5], 
    6: [6,6,6,6], 
    7: [7,9,3,1], 
    8: [8,4,2,6], 
    9: [9,1,9,1],
}

remainders = {
    0: [4,4],   
    1: [1,3],
    2: [4,4],
    3: [3,1],
    4: [4,4], 
    5: [1,1], 
    6: [4,4], 
    7: [1,3], 
    8: [4,4], 
    9: [1,1]
}


def last_digit_simple(n1, n2):
    ruler = rules[int(str(n1)[-1])]
    return 1 if n2 == 0 else ruler[(n2 % 4) - 1]

def last_digit_partial(lst):
    exponent = lst.pop()
    base = lst.pop()
    result = last_digit_simple(base, exponent)
    for x in reversed(lst):
        exponent = base
        base = result
        ruler = rules[int(str(x)[-1])]
        remainder = remainders[base]
        result = ruler[remainder[(exponent%2)] - 1]
    return result



def sliceZerosAndOnes(lst):
    for i in reversed(range(0,len(lst))):
        if lst[i] == 0:
            if i == 0: return [0]
            else: lst[i-1] = 1
    for i in range(0,len(lst)):       
        if lst[i] == 1:
            return lst[0:i]
    return lst

def last_digit(lst):
    lst_sliced = sliceZerosAndOnes(lst)
    if len(lst_sliced) == 0: return 1
    if len(lst_sliced) == 1: return int(str(lst_sliced[0])[-1])
    if len(lst_sliced) == 2: return last_digit_simple(lst_sliced[0],lst_sliced[1])
    elif len(lst_sliced) >= 3: return last_digit_partial(lst_sliced)

'''
PARA:
0: 2-4-4-4-4... (remainder 2 y 0)
1: 3-1-3-1 (remainder 3 y 1)
2: 2-4-4-4-4-4... POS (REMAINDER 2 Y 0, 0, 0...)
3: 3-1 POS (REMAINDER 3 Y 1)
4: 4 POS (REMAINDER 0)
5: 1 POS (REMAINDER 1)
6: 2-4-4-4-4-4... POS (REMAINDER 2, 0, 0, 0...)
7: 1-3 pos (remainder 1 y 3
8: 4 pos (remainder 0)
9: 1 pos (remainder 1)

'''


if __name__ == '__main__':
    print(last_digit([699568, 527915, 208553]))
    #print(last_digit_partial(635868,12003))
    #print (pow(635963,3))#2,0,0,0,0
    #print (pow(635963,13))#3,1,3,1,3
                      #0,0,0,0,0
    #print (pow(635963,23))#1,1,1,1,1
    #print (pow(635963,33))#2,0,0,0,0
    #print (pow(635963,43))#3,1,3,1,3
    #print (pow(5671,64))
'''
    print (pow(13,11))#2,0,0,0,0
    print("*********************************")
    print (pow(13,121))
    print("*********************************")
#3,1,3,1,3
                      #0,0,0,0,0
    print (pow(13,11**3))#1,1,1,1,1
    print("*********************************")

    print (pow(13,11**4))#2,0,0,0,0
    print("*********************************")

    print (pow(13,11**5))#3,1,3,1,3
    print("*********************************")

    print (pow(13,11**6))

    #0,0,0,0,0
    #1,1,1,1,1
    #2,0,0,0,0
    #3,1,3,1,3
'''


    #print(last_digit([7, 6, 21]))
    #import timeit
    #print(timeit.timeit("last_digit(10, 10 ** 10)", setup="from __main__ import last_digit"))
    #print(timeit.timeit("last_digit_pow(10, 10 ** 10)", setup="from __main__ import last_digit_pow"))

