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
        child_value = self.array[child_index] if child_index < len(self.array) else None
        return child_index, child_value

    def rchild(self, parent_index):
        """
        In an array based heap, the right child index of parent_index is 2*parent_index + 2
        """
        child_index = (2 * parent_index) + 2
        child_value = self.array[child_index] if child_index < len(self.array) else None
        return child_index, child_value

    def max_heapify(self, i):
        """
        Turn our heap into a max heap. Iteratively walk bottom to top, right to left parents
        and swap values with children if the max heap condition isn't satisfied.
        """
        value = self.array[i]
        largest = i

        lchild, lvalue = self.lchild(i)
        rchild, rvalue = self.rchild(i)
        
        if rvalue and self.array[largest] < rvalue:
            largest = rchild
        if lvalue and self.array[largest] < lvalue:
            largest = lchild

        if largest != i:
            self.array[i] = self.array[largest]
            self.array[largest] = value

        try:
            parent_index, parent_value = self.parent(i)
            self.max_heapify(parent_index)
        except RootNodeException:
            # All done
            pass

    def build_max_heap(self):
        for i in range(len(self.array)/2, -1, -1):
            self.max_heapify(i)


def test(size=10):
    h = Heap()
    h.randomize(size)
    print("Unheaped: {0}".format(h.array))
    h.build_max_heap()
    print("Max heaped: {0}".format(h.array))
    test_maxheap(h)
    return h


def test_maxheap(h):
    for i in range(0, len(h.array)):
        value = h.array[i]
        lchild_index, lchild_value = h.lchild(i)
        rchild_index, rchild_value = h.rchild(i)

        if lchild_value:
            assert value >= lchild_value, "Parent {0} at {1} !>= left child {2} at {3}".format(value, i, lchild_value, lchild_index)

        if rchild_value:
            assert value >= rchild_value, "Parent {0} at {1} !>= right child {2} at {3}".format(value, i, rchild_value, rchild_index)
