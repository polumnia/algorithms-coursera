from typing import Optional

from algorithms.linked_list import LinkedListIterator, Node, T
from algorithms.exceptions import Empty


class Queue:
    def __init__(self):
        self.first: Optional[Node[T]] = None
        self.last: Optional[Node[T]] = None
        self.size: int = 0

    def enqueue(self, item: T) -> None:
        """add item to the end of the list"""
        old_last = self.last
        self.last = Node(item, None)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last
        self.size += 1

    def dequeue(self) -> T:
        """remove element from the beginning of the list"""
        first_item = self.first.item
        self.first = self.first.next
        self.size -= 1
        if self.is_empty():
            self.last = None
        return first_item

    def is_empty(self) -> bool:
        return self.size == 0

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self.first)


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0  # index of first element within self._data

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True id queue is empty."""
        return self._size == 0

    def first(self):
        """Return the element in the front of the queue.

        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def enqueue(self, item):
        """Add element to the back of the queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        next_place = (self._front + self._size) % len(self._data)
        self._data[next_place] = item
        self._size += 1

    def dequeue(self):
        """Remove and return the first element of the queue.

        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty("Queue is empty")
        first_item = self._data[self._front]
        self._data[self._front] = None  # reclaim unused space
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data // 2))
        return first_item

    def _resize(self, new_capacity):
        """Resize to a new list of capacity >= len(self._data)."""
        old = self._data
        self._data = [None] * new_capacity
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
