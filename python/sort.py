"""
  sort

  This file is for practicing sort algorithms in Python.
"""

def bubbleSort( lst ):
  """
    The worst sort. O(n^2) time O(1) memory.
  """
  sorted = False
  while not sorted:
    sorted = True
    for i in range(len( lst ) - 1):
      if (lst[i] > lst[i+1]):
        sorted = False
        temp = lst[i+1]
        lst[i+1] = lst[i]
        lst[i] = temp

  return lst

def selectionSort( lst ):
  # Base case
  if (lst == []):
    return lst

  def findMin( lst ):
    min = (0, lst[0])
    for i in range( len(lst) ):
      if lst[i] < min[1]:
        min = i, lst[i]
    return min
  
  # Find min and put in 0 position
  m = findMin( lst )
  lst[0], lst[m[0]] = m[1], lst[0]

  # Sort the rest
  return lst[:1] +  selectionSort( lst[1:] )

if __name__ == "__main__":
  l = [7,5,8,12,3,48,72,69]
  print( bubbleSort(l) )
  print( selectionSort(l) )
      
