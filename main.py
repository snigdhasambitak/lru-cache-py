import collections


class LRUCache: 
  
  
  def __init__(self, capacity):
    self.capacity = capacity
    self.lrucache = collections.OrderedDict()
  
  def get(self, x):
    try:
      value = self.lrucache.pop(x)
      self.lrucache[x] = value
      return value
    except KeyError:
      return -1

  def set(self, x, y):
    try:
      self.lrucache.pop(x)
    except KeyError:
      if len(self.lrucache) > self.capacity:
        self.lrucache.popitem(last=False)
    self.lrucache[x] = y
    
    return list(self.lrucache)




# Test Cases

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":
  cacheOne = LRUCache(2) 
  cacheOne.set(1, 2)
  outputOne = [cacheOne.get(1)]
  check([2], outputOne)

  cacheTwo = LRUCache(2)
  cacheTwo.set(1,2)
  cacheTwo.set(2,3)
  cacheTwo.set(1,5)
  cacheTwo.set(4,5)
  cacheTwo.set(6,7)
  outputTwo = [cacheTwo.get(4)]
  cacheTwo.set(1,2)
  outputTwo.append(cacheTwo.get(3))
  check([5, -1], outputTwo)

  # Add your own test cases here
  
