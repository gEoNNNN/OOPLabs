from arrayStack import ArrayStack
from linkedStack import LinkedStack
from arrayQueue import ArrayQueue
from linkedQueue import LinkedQueue
from circluareQueue import CircularQueue
from dictStack import DictStack

class DataStructureTester:
    @staticmethod
    def test_stacks():
        print("Testing ArrayStack:")
        array_stack = ArrayStack(5)
        array_stack.push('a')
        array_stack.push('b')
        print(array_stack.pop())  # Expected: b
        print(array_stack.peek())  # Expected: a

        print("\nTesting LinkedStack:")
        linked_stack = LinkedStack()
        linked_stack.push(1)
        linked_stack.push(2)
        print(linked_stack.pop())  # Expected: 2
        print(linked_stack.peek())  # Expected: 1

        print("\nTesting DictStack:")
        dict_stack = DictStack()
        dict_stack.push('obj2', 'val1')
        dict_stack.push('obj1', 'val2')
        print(dict_stack.pop())  # Expected: ('obj1', 'val2')
        print(dict_stack.peek())  # Expected: ('obj2', 'val1')

    @staticmethod
    def test_queues():
        print("\nTesting ArrayQueue:")
        array_queue = ArrayQueue(4)
        array_queue.enqueue('car')
        array_queue.enqueue('bike')
        print(array_queue.dequeue())  # Expected: 'car'
        print(array_queue.peek())  # Expected: 'bike'

        print("\nTesting LinkedQueue:")
        linked_queue = LinkedQueue()
        linked_queue.enqueue(10)
        linked_queue.enqueue(20)
        print(linked_queue.dequeue())  # Expected: 10
        print(linked_queue.peek())  # Expected: 20

        print("\nTesting CircularQueue:")
        circular_queue = CircularQueue(3)
        circular_queue.enqueue('orange')
        circular_queue.enqueue('apple')
        circular_queue.enqueue('banana')
        print(circular_queue.dequeue())  # Expected: 'orange'
        print(circular_queue.peek())  # Expected: 'apple'
        circular_queue.enqueue('kiwi')
        print(circular_queue.dequeue())  # Expected: 'apple'
        print(circular_queue.peek())  # Expected: 'banana'

