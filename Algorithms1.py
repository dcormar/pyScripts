  #arrFiltered = list(map(lambda x: arr[x], [y for y in range(0,len(arr)) if y == 0 or arr[y] != arr[y-1]]))
def dirReduc(arr, start=0):
  dirResult = arr[0:start + 1]
  nextStart=0
  for i in range(1,len(arr)):
    if (arr[i-1] == "NORTH" and arr[i] == "SOUTH") or (arr[i-1] == "SOUTH" and arr[i] == "NORTH") or (arr[i-1] == "EAST" and arr[i] == "WEST") or (arr[i-1] == "WEST" and arr[i] == "EAST"):
      dirResult.pop(i-1)
      dirResult.extend(arr[i+1:])
      break
    else: 
      dirResult.append(arr[i])
      nextStart += nextStart
  return arr if len(arr) == len(dirResult) else dirReduc(dirResult,nextStart)



print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(['NORTH', 'WEST', 'SOUTH', 'EAST']))

#BEST:
'''
def dirReduc(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]
    
    for i in range(len(arr)-1):
        if set(arr[i:i+2]) in opposites:
            del arr[i:i+2]
            return dirReduc(arr)
    
    return arr   
'''
