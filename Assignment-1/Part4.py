# UCP HW: Linked Lists
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        
class LinkedList:
    head = Node(0)
    last = Node(0)
    theSize = 0
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
    
       
testNode1 = Node(23)
testNode2 = Node(12)
testNode3 = Node(20)
testNode4 = Node(3)
testNode5 = Node(6)

print("Testing push adds one node:")
linkedList = LinkedList()
linkedList.push(testNode1)
linkedList.printList()
print()

print("Adding nodes for test:")
linkedList.push(testNode2)
linkedList.push(testNode3)
linkedList.push(testNode4)
linkedList.push(testNode5)
linkedList.printList()
print()

print("Testing pop removes last node:")
linkedList.pop()
linkedList.printList()
print()

print("Testing remove at index 2:")
linkedList.remove(2)
linkedList.printList()
print()

print("Testing element at index 1:")
print("pointer at: ", linkedList.elementAt(1))
print("value is: ", linkedList.elementAt(1).data)
print()

print("Testing element at index doesn't exist (at 3):")
print(linkedList.elementAt(3))
print()

print("Testing size method:")
linkedList.printList()
print("size is:", linkedList.size())
print() 
