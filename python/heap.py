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
        for an array indexed from 0.
        """
        child_index = (2 * parent_index) + 1
        child_value = self.array[child_index] if child_index < len(self.array) else None
        return child_index, child_value

    def rchild(self, parent_index):
        """
        In an array based heap, the right child index of parent_index is 2*parent_index + 2
        for an array indexed from 0.
        """
        child_index = (2 * parent_index) + 2
        child_value = self.array[child_index] if child_index < len(self.array) else None
        return child_index, child_value

    def max_heap_sink(self, i):
        """
        Max heapify the tree i and it's immediate children, where the children are the roots
        of sub heaps.

        Find the largest value in the i-rooted tree and make it the new root. Max-heap-sink
        down the swapped value path to sink the swapped value to it's condition satisfying
        spot in the binary tree/heap.
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
            self.max_heap_sink(largest)

    def min_heap_sink(self, i):
        """
        Min heapify the tree i and it's immediate children, where the children are the roots
        of sub heaps.

        Find the smallest value in the i-rooted tree and make it the new root. Min-heap-sink
        down the swapped value path to sink the swapped value to it's condition satisfying
        spot in the binary tree/heap.
        """
        value = self.array[i]
        largest = i

        lchild, lvalue = self.lchild(i)
        rchild, rvalue = self.rchild(i)

        if rvalue and self.array[largest] > rvalue:
            largest = rchild
        if lvalue and self.array[largest] > lvalue:
            largest = lchild

        if largest != i:
            self.array[i] = self.array[largest]
            self.array[largest] = value
            self.min_heap_sink(largest)

    def build_max_heap(self):
        """
        Construct a max heap by iteratively applying max_heap_sink from the bottom to
        the top of the tree.

        We start iteration at length/2 as > length/2 are all leaves and thus heaps.
        """
        for i in range(len(self.array)/2, -1, -1):
            self.max_heap_sink(i)

    def build_min_heap(self):
        """
        Construct a min heap by iteratively applying min_heap_sink from the bottom to
        the top of the tree.

        We start iteration at length/2 as > length/2 are all leaves and thus heaps.
        """
        for i in range(len(self.array)/2, -1, -1):
            self.min_heap_sink(i)

    def exchange_root(self):
        """
        Remove the root (min/max) of the heap and make the last element (anything)
        the new root. Sink the new root to satisfy our heap condition.
        """
        first_value = self.array[0]
        last_value = self.array[-1]
        self.array[0] = last_value
        self.array = self.array[:-1]
        return first_value

    def max_heapsort(self):
        _sorted = []
        while self.array:
            _sorted.append(self.exchange_root())
            if self.array:
                self.max_heap_sink(0)  # sink the new root to its heapified spot
        return _sorted

    def min_heapsort(self):
        _sorted = []
        while self.array:
            _sorted.append(self.exchange_root())
            if self.array:
                self.min_heap_sink(0)  # sink the new root to its heapified spot
        return _sorted


def test(size=10):
    h = Heap()

    print("\nMaxheap tests:")
    h.randomize(size)
    print("Unheaped: {0}".format(h.array))
    h.build_max_heap()
    print("Max heaped: {0}".format(h.array))
    test_maxheap(h)
    max_heapsorted = h.max_heapsort()
    print("Max heapsorted: {0}".format(max_heapsorted))

    print("\nMinheap tests:")
    h.randomize(size)
    print("Unheaped: {0}".format(h.array))
    h.build_min_heap()
    print("Min heaped: {0}".format(h.array))
    test_minheap(h)
    min_heapsorted = h.min_heapsort()
    print("Min heapsorted: {0}".format(min_heapsorted))
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


def test_minheap(h):
    for i in range(0, len(h.array)):
        value = h.array[i]
        lchild_index, lchild_value = h.lchild(i)
        rchild_index, rchild_value = h.rchild(i)

        if lchild_value:
            assert value <= lchild_value, "Parent {0} at {1} !<= left child {2} at {3}".format(value, i, lchild_value, lchild_index)

        if rchild_value:
            assert value <= rchild_value, "Parent {0} at {1} !<= right child {2} at {3}".format(value, i, rchild_value, rchild_index)
