import collections
import random

import ipdb

import tree_utils


class BTNode(object):
    """
    Implements a node suitable for a binary tree.
    """
    def __init__(self, value, left=None, right=None, parent=None):
        """
        Binary tree constructor.
        """
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class BinaryTree(object):
    "A binary tree implementation using BTNode."

    @staticmethod
    def bfs_insert(root, value):
        """
        Use a queue based BFS to insert a new node for value at the first
        available node in the tree described by root.
        """
        queue = collections.deque([root])
        while True:
           node = queue.popleft() 
           if node.left is None:
               node.left = BTNode(value, parent=node)
               break
           else:
               queue.append(node.left)
           if node.right is None:
               node.right = BTNode(value, parent=node)
               break
           else:
               queue.append(node.right)

    @staticmethod
    def random_tree(n_values=9, max_int=9):
	values = [random.randint(1, max_int) for x in range(n_values)] 
	root = BTNode(values.pop())
	while values:
	    BinaryTree.bfs_insert(root, values.pop()) 
        return root

    @staticmethod
    def preorder_search(node, s_value, level=0):
        """
        In this implementation of a preorder search we look for the given s_value in
        the BT as implemented by the BTNode class. If we find the value, we bail early -- we're
        not traversing the whole tree unless the value doesn't appear in the tree.
        """
        if node is None:
            return False

        if node.value == s_value:
            print("Found {0}! Level {1}.".format(s_value, level))
            return True

        found = BinaryTree.preorder_search(node.left, s_value, level=level + 1)
        if not found:
	    found = BinaryTree.preorder_search(node.right, s_value, level=level + 1)
        
        if not found and level == 0:
            print("{0} is not in the tree.".format(s_value))
            return False
        else:
            return found

    @staticmethod
    def bfs(root, s_value):
        """Perform a queue based breadth-first-search of a binary tree."""
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()

            if node is None:
                continue

            if node.value == s_value:
		print("Found {0}!".format(s_value))
		return True

            queue.extend([node.left, node.right])
        print("Value {0} is not present in the tree.".format(s_value)) 
        return False


def test_bfs(n=15, display=True):
    root = BinaryTree.random_tree(n_values=n, max_int=n)
    if display:
	tree_utils.display(root)
    BinaryTree.bfs(root, 3)
    ipdb; ipdb.set_trace()


def test_preorder_search(n=15, display=True):
    root = BinaryTree.random_tree(n_values=n, max_int=n)
    if display:
	tree_utils.display(root)
    BinaryTree.preorder_search(root, 3)
    ipdb; ipdb.set_trace()


def test_binary_tree(n=15, display=True):
    root = BinaryTree.random_tree(n_values=n, max_int=n)
    if display:
	tree_utils.display(root)
    ipdb; ipdb.set_trace()


if __name__ == "__main__":
    ipdb.set_trace()
    pass
