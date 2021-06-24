# Trees - Ex1: Printing a Tree
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def print_tree(self):
        if self == None:
            return
        if self.left != None:
            self.left.print_tree()
        print(self.data, end=' ')
        if self.right != None:
            self.right.print_tree()
        
left_child = TreeNode(6, None, None)
right_child = TreeNode(3, None, None)
left = TreeNode(7, None, None)
right = TreeNode(17, left_child, right_child)
root = TreeNode(1, left, right)

root.print_tree()

'''
Output:
7 1 6 17 3
'''
