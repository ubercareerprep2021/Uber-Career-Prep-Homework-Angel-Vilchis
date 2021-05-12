# UCP HW: Reverse Linked List Methods
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        
class LinkedList:
    head = Node(0)
    last = Node(0)
    theSize = 0
    theStack = []
    def __init__(self):
        return 
    def push(self, node):
        if self.head.next == None:
            self.head.next = node
        self.last.next = node
        self.last = node
        self.theSize += 1
    def insert(self, index, node):
        curr = self.head.next
        currIndex = 0
        while curr != None:
            currIndex += 1 
            if currIndex == index:
                node.next = curr.next
                curr.next = node
                self.theSize += 1
            curr = curr.next
        return
    def remove(self, index):
        curr = self.head.next
        currIndex = 0
        while curr != None:
            currIndex += 1 
            if currIndex == index:
                curr.next = curr.next.next
                self.theSize -= 1
            curr = curr.next
        return
    def elementAt(self, index):
        curr = self.head.next
        currIndex = 0
        value = None
        while curr != None:
            currIndex += 1 
            if currIndex == index:
                value = curr.next
            curr = curr.next
        return value
    def pop(self):
        curr  = self.head.next
        while curr != None:
            if curr.next == self.last:
                value = self.last.data
                curr.next = None
            curr = curr.next
        self.theSize -= 1
        return self.last.data
    def printList(self):
        curr = self.head.next
        while curr != None:
            print(curr.data)
            curr = curr.next
    def size(self):
        return self.theSize
    def hasCycle(self):
        prevNodes = set()
        curr = self.head.next
        while curr != None:
            if curr in prevNodes:
                return True
            prevNodes.add(curr)
            curr = curr.next
        return False
    def reverseLinkedListIterative(self):
        prev = None
        curr = self.head.next
        nextNode = None
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        self.head.next = prev
        
    def reverseLinkedListRecursive(self):
        self.head.next = self.reverseLinkedListRecursiveHelper(self.head.next)
    def reverseLinkedListRecursiveHelper(self, head):
        if(head == None or head.next == None):
            return head
        reversedListHead = self.reverseLinkedListRecursiveHelper(head.next)
        head.next.next = head
        head.next = None
        return reversedListHead

    def reverseLinkedListStack(self):
        curr = self.head.next
        while curr != None:
            self.theStack.append(curr)
            curr = curr.next
        curr = self.theStack.pop()
        self.head.next = curr
        while len(self.theStack) != 1:
            curr.next = self.theStack.pop()
            curr = curr.next
        curr.next = self.theStack.pop()
        curr.next.next = None

linkedList = LinkedList()       
testNode1 = Node(23)
testNode2 = Node(12)
testNode3 = Node(20)
testNode4 = Node(3)
testNode5 = Node(6)

print("Adding nodes for test:")
linkedList.push(testNode2)
linkedList.push(testNode3)
linkedList.push(testNode4)
linkedList.push(testNode5)
linkedList.printList()
print()


print("Testing reversing linked list iteratively:")
linkedList.reverseLinkedListIterative()
linkedList.printList() 
print()

print("Testing reversing linked list recursively:")
linkedList.reverseLinkedListRecursive()
linkedList.printList() 
print()

print("Testing reversing linked list by stack:")
linkedList.reverseLinkedListStack()
linkedList.printList() 
print()
