""" 
  linkedlist.py

  Implements a basic node class capable of being chained into linked lists.
"""

class Node:
  def __init__( self, data=None, nxt=None ):
    self.data = data
    self.nxt = nxt

class LinkedList:
  def __init__(self):
    self.head = None
    self.current_node = None

  def goToEnd( self ):
    node = self.current_node
    while (node != None and node.nxt != None ):
      node = node.nxt
    self.current_node = node

  def goToStart( self ):
    self.current_node = self.head

  def prepend( self, data ):
    self.goToStart()
    node = Node( data, self.current_node )
    self.head = node
    self.current_node = node

  def append( self, data ):
    self.goToEnd()
    node = Node( data, None )
    if (self.current_node):
      self.current_node.nxt = node
    if (self.current_node == None and self.head == None):
      self.head = node
    self.current_node = node

  def printList( self ):
    self.goToStart()
    node = self.current_node
    while (node):
      print( str(node.data) )
      node = node.nxt

if __name__ == "__main__":
  l = LinkedList()

  l.append("Hello")
  l.append("World!")
  l.printList()

  l.prepend("Kyle says")
  l.printList()

