def last_digit(n1, n2):
    if n2 == 0:
        return 1
    cycle = [n1 % 10]
    while True:
        nxt = (cycle[-1] * n1) % 10
        if nxt == cycle[0]:
            break
        cycle.append(nxt)
    return cycle[(n2 - 1) % len(cycle)]


def last_digit_pow(n1, n2):
    return pow(n1, n2, 10)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("last_digit(10, 10 ** 10)", setup="from __main__ import last_digit"))
    print(timeit.timeit("last_digit_pow(10, 10 ** 10)", setup="from __main__ import last_digit_pow"))

#BEST:
'''
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
def last_digit(n1, n2):
    ruler = rules[int(str(n1)[-1])]
    return 1 if n2 == 0 else ruler[(n2 % 4) - 1]
'''

