import random

class Node(object):
    """
    Implements a node suitable for a binary search tree with duplicate elements.
    Duplication is tracked with a count attribute.
    """
    def __init__(self, value, left=None, right=None):
        """
        The constructor instantiates the instance with an inital count of 1.
        Left/right elements may be specified or left as None.
        """
        self.value = value
        self.count = 1
        self.left = left
        self.right = right

    @staticmethod
    def ordered_insert(node, value):
        """
        Insert a new value, in order, treating node as the root of a BST as
        defined by the Node class. Duplicate values with result in an increased
        count.

        This function is implemented as a staticmethod which can be called
        recursively.
        """
        if value == node.value:
            node.count += 1
        elif value < node.value:
            if node.left is not None:
                Node.ordered_insert(node.left, value)
            else:
                node.left = Node(value)
        elif value > node.value:
            if node.right is not None:
                Node.ordered_insert(node.right, value)
            else:
                node.right = Node(value)


if __name__ == "__main__":
    values = [random.randint(1, 9) for x in range(20)] 
    root = Node(values.pop())
    while values:
        Node.ordered_insert(root, values.pop()) 
    import ipdb; ipdb.set_trace()
    pass
