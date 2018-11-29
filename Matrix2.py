def wave(str):
    return [''.join([str[i] if i != j else str[i].capitalize() for i in range(0,len(str))]) for j in range(0,len(str)) if str[j] != " "]




print (wave("hello my darling"))


#BEST: return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]