class StackInterface:
    def push(self, item):
        """Add an item to the top of the stack."""
        raise NotImplementedError

    def pop(self):
        """Remove the top item from the stack."""
        raise NotImplementedError

    def peek(self):
        """Look at the top item without removing it."""
        raise NotImplementedError

    def is_empty(self):
        """Check if the stack is empty."""
        raise NotImplementedError

    def size(self):
        return len(self.stack)