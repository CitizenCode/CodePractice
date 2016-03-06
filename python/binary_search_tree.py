import random

import ipdb

from binary_tree import BTNode
import tree_utils


class BSTNode(BTNode):
    """
    Implements a node suitable for a binary search tree with duplicate elements.
    Duplication is tracked with a count attribute.
    """
    def __init__(self, value, left=None, right=None, parent=None):
        """
        The constructor instantiates the instance with an inital count of 1.
        Left/right elements may be specified or left as None.
        """
        super(BSTNode, self).__init__(value, left=None, right=None, parent=None)
        self.count = 1


class BinarySearchTree(object):
    """A binary search tree implemention using BSTNode"""

    @staticmethod
    def ordered_insert(node, value):
        """
        Insert a new value, in order, treating node as the root of a BST as
        defined by the BSTNode class. Duplicate values with result in an increased
        count.

        This function is implemented as a staticmethod which can be called
        recursively.
        """
        if value == node.value:
            node.count += 1
        elif value < node.value:
            if node.left is not None:
                BinarySearchTree.ordered_insert(node.left, value)
            else:
                node.left = BSTNode(value)
        elif value > node.value:
            if node.right is not None:
                BinarySearchTree.ordered_insert(node.right, value)
            else:
                node.right = BSTNode(value)

    @staticmethod
    def random_bst(n_values=9, max_int=9):
        """
        Generate a random binary search tree.
        """
	values = [random.randint(1, max_int) for x in range(n_values)] 
	root = BSTNode(values.pop())
	while values:
	    BinarySearchTree.ordered_insert(root, values.pop()) 
        return root

    @staticmethod
    def binary_search(node, value, level=0):
        """
        Recursively peform a binary search for value.
        """
        if value == node.value:
            print("Found {0} at level {1}!".format(value, level))
            return True

        found = False
        if value < node.value:
            if node.left is not None:
                found = BinarySearchTree.binary_search(node.left, value, level=level + 1)
        elif value > node.value:
            if node.right is not None:
                found = BinarySearchTree.binary_search(node.right, value, level=level + 1)

        if not found and level == 0:
            print("Value {0} does not appear in the tree.".format(value))
        else:
            return found


def test_display():
    root = BinarySearchTree.random_bst(n_values=15, max_int=15)
    tree_utils.display(root)
    ipdb; ipdb.set_trace()


def test_binary_search(n=15, display=True):
    root = BinarySearchTree.random_bst(n_values=n, max_int=n)
    if display:
	tree_utils.display(root)
    BinarySearchTree.binary_search(root, 3)
    ipdb; ipdb.set_trace()


if __name__ == "__main__":
    ipdb.set_trace()
    pass
