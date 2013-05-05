""" 
  dbllinkedlist.py

  Implements a basic node class capable of being chained into doubly linked lists.
"""

class DblNode:
  def __init__( self, data=None, left=None, right=None ):
    self.data = data
    self.left = left
    self.right = right
    
class DblLinkedList:
  def __init__(self):
    self.current_node = None

  def goToEnd( self ):
    node = self.current_node
    while (node != None and node.right != None):
      node = node.right
    self.current_node = node

  def goToStart( self ):
    node = self.current_node
    while (node != None and node.left != None):
      node = node.left
    self.current_node = node

  def append( self, data ):
    self.goToEnd()
    node = DblNode( data, self.current_node, None )
    if (self.current_node):
        self.current_node.right = node
    self.current_node = node

  def prepend( self, data ):
    self.goToStart()
    node = DblNode( data, None, self.current_node )
    if (self.current_node):
        self.current_node.left = node
    self.current_node = node

  def RightToLeftPrintList( self ):
    self.goToEnd()
    node = self.current_node
    while (node):
      print( str(node.data) )
      node = node.left

  def LeftToRightPrintList( self ):
    self.goToStart()
    node = self.current_node
    while (node):
      print( str(node.data) )
      node = node.right

if __name__ == "__main__":
  ll = DblLinkedList()
  ll.append("Hello")
  ll.append("World")
  ll.LeftToRightPrintList()
  ll.RightToLeftPrintList()
