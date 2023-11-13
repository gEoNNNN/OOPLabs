class DoubleStack:
    def __init__(self):
        self.main_stack = ArrayStack()
        self.min_stack = ArrayStack()

    def push(self, item):
        self.main_stack.push(item)
        if self.min_stack.is_empty() or item <= self.min_stack.peek():
            self.min_stack.push(item)

    def pop(self):
        item = self.main_stack.pop()
        if item == self.min_stack.peek():
            self.min_stack.pop()
        return item

    def min(self):
        if self.min_stack.is_empty():
            raise IndexError("min from empty stack")
        return self.min_stack.peek()
