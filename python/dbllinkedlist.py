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

  def goToRightEnd( self ):
    node = self.current_node
    while (node != None and node.right != None):
      node = node.right
    self.current_node = node

  def goToLeftEnd( self ):
    node = self.current_node
    while (node != None and node.left != None):
      node = node.left
    self.current_node = node

  def rightAddNode( self, data ):
    self.goToRightEnd()
    node = Node( data, self.current_node, None )
    self.current_node = node

  def leftAddNode( self, data ):
    self.goToLeftEnd()
    node = Node( data, None, self.current_node )
    self.current_node = node

  def RightToLeftPrintList( self ):
    self.goToRightEnd()
    node = self.current_node
    while (node):
      print( str(node.data) )
      node = node.left

  def LeftToRightPrintList( self ):
    self.goToLeftEnd()
    node = self.current_node
    while (node):
      print( str(node.data) )
      node = node.right
