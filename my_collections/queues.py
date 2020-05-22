from typing import Optional, TypeVar, Generic
from dataclasses import dataclass

from my_collections.linked_list import LinkedListIterator, Node, T

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
