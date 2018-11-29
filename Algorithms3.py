def move_zeros(array):
    arraySize = len(array)
    print (arraySize)
    array_nonZeros = [x for x in array if type (x) is bool or x != 0]
    return (array_nonZeros + ([0 for y in range(arraySize - len(array_nonZeros))]))


print (move_zeros([0,1,None,2,False,1,0]))