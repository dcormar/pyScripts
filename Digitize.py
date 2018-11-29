def digitize(x):
  return list(reversed(list(map(int, str(x)))))

print(digitize(35231))

#BEST: return map(int, str(n)[::-1])