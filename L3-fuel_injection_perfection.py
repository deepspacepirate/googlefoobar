# space complexity O(1)
# time complexity O(log(n)): 

def answer(n):
  num = int(n)
  ops = 0
  
  while (num > 1):
    # how many zeroes after least significant bit
    rot = (num & -num).bit_length()-1
    if (rot > 0):
      num >>= rot
      ops += rot

    if (num > 4):
      if (num&3 == 3): num = (num+1) >> 2
      else           : num = (num-1) >> 2
      ops += 3
    elif (num == 3): return ops + 2

  return ops