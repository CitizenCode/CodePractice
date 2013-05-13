"""
  sort

  This file is for practicing sort algorithms in Python.
"""

def bubbleSort( list ):
"""
  The worst sort. O(n^2) time O(1) memory.
"""
  sorted = False
  while not sorted:
    sorted = True
    for i in range(len( list ) - 1):
      if (list[i] > list[i+1]):
        sorted = False
        temp = list[i+1]
        list[i+1] = list[i]
        list[i] = temp

  return list

def selectionSort( list ):
  def findMin( list ):
    min = (0, list[0])
    for i in range( len(list) ):
      if list[i] < min:
        min = i, list[i]
    return min
  
  m = findMin( list )
  list[0], list[m[0]] = m[1], list[0]
  return [list[0]].extend( selectionSort( list[1:] ) )

if __name__ == "__main__":
  l = [1,7,3,5,8]
  print( bubbleSort(l) )
  print( selectionSort(l) )
      
