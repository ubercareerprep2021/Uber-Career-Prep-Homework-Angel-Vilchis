# UCP HW: Stacks & Queues
class Stack:
    TheStack = []
    def _init_(self):
        return
    def push(self, item):
        self.TheStack.append(item)
    def pop(self):
        if self.isEmpty():
            print("Stack is empty, cannot use pop method.")
            return
        else:
            return self.TheStack.pop()
    def top(self):
        if self.isEmpty():
            print("Stack is empty, cannot use top method.")
            return
        else:
            return self.TheStack[-1]
    def isEmpty(self):
        return len(self.TheStack) == 0
    def size(self):
        return len(self.TheStack)
    def min(self):
        if (self.TheStack.isEmpty()):
            print("Stack is empty, no minimum values.")
        else:
            return currMin
    
class Queue:
    TheQueue = []
    def _init_(self):
        return
    def enqueue(self, item):
        self.TheQueue.append(item)
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty, cannot use dequeue method.")
            return
        else:
            return self.TheQueue.pop(0)
    def rear(self):
        if self.isEmpty():
            print("Queue is empty, cannot use rear method.")
            return
        else:
            return self.TheQueue[-1]
    def front(self):
        if self.isEmpty():
            print("Queue is empty, cannot use front method.")
            return
        else:
            return self.TheQueue[0]
    def size(self):
        return len(self.TheQueue)
    def isEmpty(self):
        return len(self.TheQueue) == 0
    
    
def main():
    # STACK DRIVER (INTS)
    myStack = Stack()
    myStack.push(42)
    print ("Top of stack: ", myStack.top())
    # prints “Top of stack: 42”
    print ("Size of stack: ", myStack.size())
    # prints “Size of stack: 1”
    popped_value = myStack.pop()
    print ("Popped value: " , popped_value)
    # prints “Popped value: 42”
    print ("Size of stack: ", myStack.size())
    # prints “Size of stack: 0”
    myStack.pop()
    myStack.top()
    # tries pop and top methods on empty stack
    print()
    
    # STACK DRIVER (STRINGS) 
    myStack = Stack()
    myStack.push("Hello")
    myStack.push("World")
    print ("Top of stack: ", myStack.top())
    # prints “Top of stack: World”
    print ("Size of stack: ", myStack.size())
    # prints “Size of stack: 2”
    print("Popped value:", myStack.pop())
    # prints “Popped value: World”
    print ("Size of stack: ", myStack.size())
    # prints “Size of stack: 1”
    print("Popped value:", myStack.pop())
    myStack.pop()
    myStack.top()
    # tries pop and top methods on empty stack
    
    print()

    # QUEUE DRIVER (INTS)
    myQueue = Queue()
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    print ("Size of queue: ", myQueue.size())
    # prints “Size of queue: 3”
    print ("Front of queue: ", myQueue.front())
    # prints “Front of queue: 1”
    print ("Rear of queue: ", myQueue.rear())
    # prints “Rear of queue: 3”
    print("Dequeue item: ", myQueue.dequeue())
    # prints “Dequeued item: 1”
    print("Dequeue item: ", myQueue.dequeue())
    print("Dequeue item: ", myQueue.dequeue())
    # dequeues 2 followed by 3
    myQueue.dequeue()
    myQueue.rear()
    myQueue.front()
    # tries dequeue, rear, front methods on empty queue

    print()
    
    # QUEUE DRIVER (STRINGS)
    myQueue = Queue()
    myQueue.enqueue("Hello")
    myQueue.enqueue("World")
    myQueue.enqueue("Hi!")
    print ("Size of queue: ", myQueue.size())
    # prints “Size of queue: 3”
    print ("Front of queue: ", myQueue.front())
    # prints “Front of queue: Hello”
    print ("Rear of queue: ", myQueue.rear())
    # prints “Rear of queue: Hi!”
    print("Dequeue item: ", myQueue.dequeue())
    # prints “Dequeued item: Hello”
    print("Dequeue item: ", myQueue.dequeue())
    print("Dequeue item: ", myQueue.dequeue())
    # dequeues World followed by Hi!
    myQueue.dequeue()
    myQueue.rear()
    myQueue.front()
    # tries dequeue, rear, front methods on empty queue
main()
