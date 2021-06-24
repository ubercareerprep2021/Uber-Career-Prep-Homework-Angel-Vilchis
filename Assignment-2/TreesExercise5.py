class ListPhoneBook:
	def __init__(self):
		self.numbers = []
	def size(self):
		return len(self.numbers)

	def insert(self, name, phone_number):
		return self.numbers.append([name, phone_number])

	def find(self, name):
		number_idx = 0
		name_idx = 1
		for idx in range(self.size()):
			if name == self.numbers[idx][number_idx]:
				return self.numbers[idx][name_idx]
		not_found = -1
		return not_found

# ListPhoneBook Test
list_phone_book = ListPhoneBook()

list_phone_book.insert('Jeff', 4081525648)
list_phone_book.insert('Terrance', 6696381325)
list_phone_book.insert('Joseph', 4086535492)
list_phone_book.insert('Devin', 6691456532)

print(list_phone_book.size(), 4)
print(list_phone_book.find('Devin'), 6691456532)
print(list_phone_book.find('John'), -1)

print()

class BinarySearchTreePhoneBook:
    def __init__(self, root):
    	self.root = root
    	self.num_nodes = 1

    def size(self):
    	return self.num_nodes

    def insert(self, node, root=''):
        if self.root == None:
            self.root = node 
            return
        if root == '':
            root = self.root
        if root == None:
            return False
        if node.name >= root.name:
            pos_found = self.insert(node, root.right)
            if not pos_found:
                root.right = node
                self.num_nodes += 1
                pos_found = True
        else:
            pos_found = self.insert(node, root.left)
            if not pos_found:
                root.left = node
                self.num_nodes += 1
                pos_found = True
        return pos_found
    
    def find(self, name, root=''):
        if root == '':
            root = self.root
        if root == None:
        	not_found = -1
        	return not_found
        if name == root.name:
            return root.number
        elif name > root.name:
            val_found = self.find(name, root.right)
        else:
            val_found = self.find(name, root.left)
        return val_found

    class Node:
        def __init__(self, name, number, left=None, right=None):
            self.name = name
            self.number = number
            self.left = left
            self.right = right

# BST PhoneBook Test
root_node = BinarySearchTreePhoneBook.Node('Jeff', 4081525648)
bst_phone_book = BinarySearchTreePhoneBook(root_node)

node_1 = BinarySearchTreePhoneBook.Node('Terrance', 6696381325)
bst_phone_book.insert(node_1)
node_2 = BinarySearchTreePhoneBook.Node('Joseph', 4086535492)
bst_phone_book.insert(node_2)
node_3 = BinarySearchTreePhoneBook.Node('Devin', 6691456532)
bst_phone_book.insert(node_3)

print(bst_phone_book.size(), 4)
print(bst_phone_book.find('Devin'), 6691456532)
print(bst_phone_book.find('John'), -1)

'''
Output
4 4
6691456532 6691456532
-1 -1

4 4
6691456532 6691456532
-1 -1
'''
