from math import log, ceil
def bouncingBall(h, bounce, window):
    return -1 if (h <= 0 or bounce <= 0 or bounce >= 1 or window >= h) else (ceil(log(window/h,bounce))*2 - 1)

print (bouncingBall(30, 0.66, 1.5))



'''
CON EL SIGTE CÓDIGO, DA ERROR DE "RecursionError: maximum recursion depth exceeded while calling a Python object"

if direction == 'DOWN' and h >= window:
      print("Ball " + direction + " and higher than window. Counter = " + str(counter))
      return bouncingBall(bounce*h, bounce, window, counter + 1, 'UP')
    elif direction == 'UP' and h >= window:
      print("Ball " + direction + " and higher than window. Counter = " + str(counter))
      return bouncingBall(h, bounce, window, counter + 1, 'DOWN')
    else: 
      print("Ball " + direction + " and lower than window. Counter = " + str(counter))
      return counter
'''