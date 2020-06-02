from algorithms.exceptions import Empty


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage"""
    def __init__(self):
        """Create an empty stack"""
        self._data = list()

    def push(self, item):
        """Add element item to the top of the stack"""
        self._data.append(item)

    def pop(self):
        """Remove and return the element at the top of the stack.

        Raise Empty exception if stack is empty"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def top(self):
        """Return the element at the top of the stack.

        Raise Empty exception if stack is empty"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def is_empty(self):
        """Return True if stack is empty"""
        return len(self._data) == 0

    def __len__(self):
        """Return number of elemets in the stack"""
        return len(self._data)
