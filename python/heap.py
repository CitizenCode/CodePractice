"""
heap

A heap is a binary tree that we fill from top to bottom, left to right.
We also impose one of two properties, creating either a max or min heap,
when the parent nodes are 'greater' or 'less' than the child nodes.

A heap can be convieniently stored as an array.
"""
import random


class RootNodeException(Exception):
    # We've iterated to the root node
    pass


class Heap(object):
    def __init__(self):
        self.array = []

    def randomize(self, size, max_value=None):
        """
        Generate a random initial heap state. The initial state does not satisfy
        a max or min heap condition.

        :param int size: The number of nodes in the initial heap.
        """
        max_value = max_value or size
        self.array = [random.randint(0, max_value) for s in range(0, size)]

    def parent(self, child_index):
        """
        In an array based heap, the parent of index child_index can be found at
        floor((child_index - 1)/ 2) for an array indexed from 0.
        """
        if child_index == 0:
            raise RootNodeException()

        parent_index = (child_index - 1)/2
        return parent_index, self.array[parent_index]

    def lchild(self, parent_index):
        """
        In an array based heap, the left child index of parent_index is 2*parent_index + 1
        """
        child_index = (2 * parent_index) + 1
        return child_index, self.array[child_index]

    def rchild(self, parent_index):
        """
        In an array based heap, the right child index of parent_index is 2*parent_index + 2
        """
        child_index = (2 * parent_index) + 2
        return child_index, self.array[child_index]

    def max_heapify(self):
        """
        Turn our heap into a max heap.
        """
        for i in range(len(self.array) - 1, 0, -1):
            value = self.array[i]
            parent_index, parent_value = self.parent(i)
            if value > parent_value:
                self.array[parent_index] = value
                self.array[i] = parent_value

def test(size=10):
    h = Heap()
    h.randomize(size)
    print("Unheaped: {0}".format(h.array))
    h.max_heapify()
    print("Max heaped: {0}".format(h.array))
    test_maxheap(h)
    return h


def test_maxheap(h):
    for i in range(0, len(h.array)):
        try:
            assert h.array[i] >= h.lchild(i)[1]
            assert h.array[i] >= h.rchild(i)[1]
        except IndexError:
            # No child
            pass
