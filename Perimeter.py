import numpy as np
def get1Dperimeter(m):
    print ("matrix to use is:")
    m_matrix = [ list(m[i]) for i in range (len(m)) ]
    print(np.matrix(m_matrix))
    totalPerimeter1D = 0
    counter = 1
    for line in m:
        linesum = 1 if line [0] == 'X' else 0
        linesum += 1 if linesum == 1 and line[1] == 'O' else 0
        for i in range(1,len(line)-1):
            if line[i] == 'X':
                if line[i-1] == 'O' and line[i+1] == 'O': linesum +=2 
                elif line[i-1] == 'X' and line[i+1] == 'O' or line[i-1] == 'O' and line[i+1] == 'X': linesum +=1
        linesum += 2 if line [len(line)-1] == 'X' and line [len(line)-2] == 'O' else 1 if line [len(line)-1] == 'X' else 0
        totalPerimeter1D += linesum
        print ("line " + str(counter) + ": " + str(linesum))
    print ('Total perimeter 1D: ' + str(totalPerimeter1D))
    return totalPerimeter1D

def transpose (arr):
    arr_transposed=[]
    for j in range (len(arr[0])):
        yLine = '' 
        for i in range(len(arr)):
            yLine += arr[i][j]
        arr_transposed.append(''.join(str(yLine)))
    return arr_transposed

def land_perimeter(arr):
    totalPerimeter = 0
    if len(arr) == 1 and len (arr[0]) == 1:
        totalPerimeter = 4 if arr[0][0] == 'X' else 0
    else:
        totalPerimeterY = get1Dperimeter(arr)   
        totalPerimeterX = get1Dperimeter(transpose(arr))
        totalPerimeter = totalPerimeterX + totalPerimeterY
    return 'Total land perimeter: '+ str(totalPerimeter)

#print (land_perimeter(['XOOXO', 'XOOXO', 'OOOXO', 'XXOXO', 'OXOOO'] ))
print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]))


'''
def land_perimeter(arr):
   
    I,J = len(arr),len(arr[0])
    
    P = 0
    for i in range(I):
        for j in range(J):
            if arr[i][j] == 'X':
                if i == 0   or arr[i-1][j] == 'O': P += 1
                if i == I-1 or arr[i+1][j] == 'O': P += 1
                if j == 0   or arr[i][j-1] == 'O': P += 1
                if j == J-1 or arr[i][j+1] == 'O': P += 1
                   
                  
    return 'Total land perimeter: ' + str(P)
'''
