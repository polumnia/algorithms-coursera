from typing import Optional

from algorithms.linked_list import LinkedListIterator, Node, T, DLLNode

class Deque:
    def __init__(self):
        self.first: Optional[Node[T]] = None
        self.last: Optional[Node[T]] = None
        self.size: int = 0

    def is_empty(self):
        return self.size == 0

    def add_first(self, item):
        """add item to the beginning of the list"""
        old_first = self.first
        self.first = Node(item, old_first)
        if self.is_empty():
            self.last = self.first
        self.size += 1

    def add_last(self, item):
        """add item to the end of the list"""
        old_last = self.last
        self.last = Node(item, None)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last
        self.size += 1

    def remove_first(self):
        """remove element from the beginning of the list"""
        first_item = self.first.item
        self.first = self.first.next
        self.size -= 1
        if self.is_empty():
            self.last = None
        return first_item

    def remove_last(self):
        cur_node = self.first
        while cur_node.next.next:
            cur_node = cur_node.next
        last_item = cur_node.next.item
        cur_node.next = None
        self.last = cur_node
        self.size -= 1
        if self.is_empty():
            self.first = None
        return last_item

    def __iter__(self):
        return LinkedListIterator(self.first)


class DLLDeque:
    def __init__(self):
        self.first: Optional[DLLNode[T]] = None
        self.last: Optional[DLLNode[T]] = None
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def add_first(self, item: T) -> None:
        old_first = self.first
        self.first = DLLNode(item, old_first, None)
        if self.is_empty():
            self.last = self.first
        else:
            old_first.previous = self.first
        self.size += 1

    def add_last(self, item: T) -> None:
        old_last = self.last
        self.last = DLLNode(item, None, old_last)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last
        self.size += 1

    def remove_first(self) -> T:
        first_item = self.first.item
        self.first = self.first.next
        self.first.previous = None
        self.size -= 1
        if self.is_empty():
            self.last = None
        return first_item

    def remove_last(self) -> T:
        last_item = self.last.item
        self.last = self.last.previous
        self.last.next = None
        self.size -= 1
        if self.is_empty():
            self.first = None
        return last_item

    def __iter__(self):
        return LinkedListIterator(self.first)


if __name__ == "__main__":
    l = ['to', 'be', 'or', 'not', 'to', 'be']
    q = Deque()
    for elem in l:
        q.add_last(elem)

    for q_elem in q:
        print(q_elem)
