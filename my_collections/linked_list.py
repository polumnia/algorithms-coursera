from typing import Optional, TypeVar, Generic
from dataclasses import dataclass

T = TypeVar("T")

@dataclass
class Node(Generic[T]):
    item: T
    next: Optional['Node[T]']

class LinkedListIterator:
    def __init__(self, first: Node[T]):
        self.current = first

    def __next__(self):
        try:
            item = self.current.item
            self.current = self.current.next
        except AttributeError:
            raise StopIteration
        return item
