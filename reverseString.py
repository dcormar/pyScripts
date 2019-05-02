def super_size(n):
    numbers = []
    for x in str(n): numbers.append (x)
    numbers.sort(reverse = True)
    return int(''.join(numbers))