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
    self.current_node = None

  def newNode( self, data ):
    node = Node( data, self.current_node )
    self.current_node = node

  def printList( self ):
    node = self.current_node
    while (node):
      print( str(node.data) )
      node = node.nxt
