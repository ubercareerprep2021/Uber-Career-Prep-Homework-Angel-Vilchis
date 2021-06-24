# Trees - Ex4: Implement a BST
class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, key_node, root=''):
        if root == '':
            root = self.root
        if root == None:
            return False
        if key_node.key >= root.key:
            pos_found = self.insert(key_node, root.right)
            if not pos_found:
                root.right = key_node
                pos_found = True
        else:
            pos_found = self.insert(key_node, root.left)
            if not pos_found:
                root.left = key_node
                pos_found = True
        return pos_found
    
    def find(self, key, root=''):
        if root == '':
            root = self.root
        if root == None:
            return False
        if key == root.key:
            return True
        elif key > root.key:
            found = self.find(key, root.right)
        else:
            found = self.find(key, root.left)
        return found
            
        
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

# Testing Insert
node_0 = BST.Node(16)
bst = BST(node_0)

node_1 = BST.Node(10)
bst.insert(node_1)
print(node_0.left.key) # 10

node_2 = BST.Node(21)
bst.insert(node_2)
print(node_0.right.key) # 21

node_3 = BST.Node(7)
bst.insert(node_3)
print(node_0.left.left.key) # 7

node_4 = BST.Node(13)
bst.insert(node_4)
print(node_0.left.right.key) # 13

node_5 = BST.Node(18)
bst.insert(node_5)
print(node_0.right.left.key) # 18

node_6 = BST.Node(29)
bst.insert(node_6)
print(node_0.right.right.key) # 29

node_7 = BST.Node(99)
bst.insert(node_7)
print(node_0.right.right.right.key) # 99

# Testing Find
print(bst.find(10)) # T
print(bst.find(21)) # T
print(bst.find(7))  # T
print(bst.find(13)) # T
print(bst.find(18)) # T
print(bst.find(9))  # F
print(bst.find(2))  # F


'''
Output:
10
21
7
13
18
29
99
True
True
True
True
True
False
False
'''

