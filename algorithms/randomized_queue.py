from typing import TypeVar, List

T = TypeVar("T")


class RandomizedQueue:
    def __init__(self):
        self.items: List[T] = list()
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def enqueue(self, item: T):
        self.items.append(item)

    def dequeue(self):
        pass

    def sample(self):
        pass
