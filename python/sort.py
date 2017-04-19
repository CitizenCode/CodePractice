"""
  sort

  This file is for practicing sorting algorithms in Python.
"""

def bubbleSort( lst ):
  """
    The worst sort. O(n^2) time avg and worst case, O(1) memory.
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
  """
    Pretty bad still, O(n^2) avg and worst case time, O(1) memory.
    But do these O's count recursion?
  """
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

def mergeSort( lst ):
  """
    O(n log n) avg and worst time, memory depends
  """
  if (len(lst) <= 1):
    return lst # The list of length 1 (0) is sorted by definition

  def merge( left, right ):
    result = []
    while( len(left) > 0 and len(right) > 0 ):
      if (left[0] < right[0]):
        result.append(left[0])
        left = left[1:]
      else:
        result.append(right[0])
        right = right[1:]
    if (len( left ) > 0):
      result = result + left
    if (len( right ) > 0):
      result = result + right

    return result

  mid = int(len( lst ) / 2)
  left, right = lst[:mid], lst[mid:]
  left = mergeSort( left )
  right = mergeSort( right )

  return merge( left, right )

def quickSort( lst ):
  """
    O(n log n) avg O(n^2) worst time, O( log n ) memory
  """
  if (len(lst) < 1):
    return lst

  # Naive pivot
  pivot = lst.pop( int(len(lst) / 2) )
  left = []
  right = []
  for l in lst:
    if l < pivot:
      left.append(l)
    else:
      right.append(l)

  return quickSort( left ) + [pivot] + quickSort( right )


if __name__ == "__main__":
  l = [7,5,8,12,122,35,55,1,3,48,72,69]
  print( "Unsorted: " + str(l) )
  print( "Bubble: " + str(bubbleSort(l)) )
  print( "Selection: " + str(selectionSort(l)) )
  print( "Merge: " + str(mergeSort(l)) )
  print( "Quick: " + str(quickSort(l)) )
