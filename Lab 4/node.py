from stackInterface import StackInterface


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack(StackInterface):
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.value

    def is_empty(self):
        return self.head is None