import re

def reducePoly (poly_matrix):
    resultString = ''
    result = []
    for i in range(0,len(poly_matrix)):
        if len(result) == 0: result.append(poly_matrix[i])
        else :
            if result[len(result)-1][1] == poly_matrix[i][1]:
                operation_result=eval (result[len(result)-1][0] + poly_matrix[i][0]) 
                if operation_result != 0: result[len(result)-1][0] = str(operation_result)
                else: result.pop()
            else: 
                result.append(poly_matrix[i])
    if result[0][0][0] == '+': result[0][0] = result[0][0][1:]
    if result[0][0] == '1': result[0][0] = ''
    for i in range(0,len(result)):
        if result[i][0] in ('1','+1'): result[i][0] = '+'
        elif result[i][0] == '-1': 
            result[i][0] = '-'
        resultString += ''.join(result[i])
    return resultString

def simplify (poly):
    sign_element_list = list(filter(None, re.split(r'(\W)',poly.replace(' ', ''))))
    if not re.match ('^\W', sign_element_list[0]): sign_element_list = ['+'] + sign_element_list
    poly_matrix = [[sign_element_list[x], ''.join(sorted(sign_element_list[x+1] if sign_element_list[x+1][0].isdigit() else '1'+sign_element_list[x+1]))] for x in range(0,len(sign_element_list)) if x % 2 == 0]
    for i in range(0,len(poly_matrix)): 
        num_and_vars = re.split('(\d)', poly_matrix[i][1])
        poly_matrix[i][0] = poly_matrix[i][0] + num_and_vars[-2]
        poly_matrix[i][1] = num_and_vars[-1]
    poly_matrix.sort(key=lambda x:x[1])
    poly_matrix.sort(key=lambda x:len(x[1]))
    return reducePoly(poly_matrix)

print(simplify('-abc+3a+2ac'))

#si se usa paréntesis en regex, entonces también se incluyen los delimitadores como elementos de la lista



'''
BEST:

def simplify(poly):
    # I'm feeling verbose today
    
    # get 3 parts (even if non-existent) of each term: (+/-, coefficient, variables)
    import re
    matches = re.findall(r'([+\-]?)(\d*)([a-z]+)', poly)
    
    # get the int equivalent of coefficient (including sign) and the sorted variables (for later comparison)
    expanded = [[int(i[0] + (i[1] if i[1] != "" else "1")), ''.join(sorted(i[2]))] for i in matches]
    
    # get the unique variables from above list. Sort them first by length, then alphabetically
    variables = sorted(list(set(i[1] for i in expanded)), key=lambda x: (len(x), x))
    
    # get the sum of coefficients (located in expanded) for each variable
    coefficients = {v:sum(i[0] for i in expanded if i[1] == v) for v in variables}
    
    # clean-up: join them with + signs, remove '1' coefficients, and change '+-' to '-'
    return '+'.join(str(coefficients[v]) + v for v in variables if coefficients[v] != 0).replace('1','').replace('+-','-')

'''