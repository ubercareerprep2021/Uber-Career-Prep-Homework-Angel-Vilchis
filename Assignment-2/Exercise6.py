import time

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

class ListPhoneBookError(Exception):
    pass

class BinarySearchTreePhoneBook:
    def __init__(self, root=None):
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

class BSTPhoneBookError(Exception):
    pass

# List Test
phone_book = ListPhoneBook()
data = open('data.csv', 'r')
data_lines = data.read().splitlines()

time_before_insert = time.perf_counter()
for line in data_lines:
    name_num = line.split(',')
    phone_book.insert(name_num[0], int(name_num[1]))
time_to_insert = time.perf_counter()-time_before_insert
if phone_book.size() != 1000000:
    raise ListPhoneBookError("size() not returning 1000000 for ListPhoneBook.")
data.close()

search = open('search.txt', 'r')
search_lines = search.read().splitlines()
time_before_find = time.perf_counter()
find_call_count = 0
for line in search_lines:
    find_call_count += 1
    if phone_book.find(line) == -1: 
        raise ListPhoneBookError("Error using find method for ListPhoneBook.")
if find_call_count != 1000:
    raise ListPhoneBookError("find() not called 1000 times for ListPhoneBook.")
search.close()
time_to_find = time.perf_counter() - time_before_find

print("LIST IMPLEMENTATION: ")
print("Insert took {} milliseconds".format(int(time_to_insert*1000)))
print("The size of the PhoneBook is {}".format(phone_book.size()))
print("find() was called {} times".format(find_call_count))
print("Search took {} milliseconds".format(int(time_to_find*1000)))

print() 

# Binary Search Tree Test
phone_book2 = BinarySearchTreePhoneBook()
data = open('data.csv', 'r')
data_lines = data.read().splitlines()

time_before_insert = time.perf_counter()
for line in data_lines:
    name_num = line.split(',')
    node = BinarySearchTreePhoneBook.Node(name_num[0], int(name_num[1]))
    phone_book2.insert(node)
time_to_insert = time.perf_counter()-time_before_insert
if phone_book2.size() != 1000000:
    raise BSTPhoneBookError("size() not returning 1000000 for BSTPhoneBook.")
data.close()

search = open('search.txt', 'r')
search_lines = search.read().splitlines()
time_before_find = time.perf_counter()
find_call_count = 0
for line in search_lines:
    find_call_count += 1
    if phone_book2.find(line) == -1: 
        raise BSTPhoneBookError("Error using find method for BSTPhoneBook.")
if find_call_count != 1000:
    raise BSTPhoneBookError("find() not called 1000 times for BSTPhoneBook.")
search.close()
time_to_find = time.perf_counter() - time_before_find

print("BST IMPLEMENTATION:")
print("Insert took {} milliseconds".format(int(time_to_insert*1000)))
print("The size of the PhoneBook is {}".format(phone_book2.size()))
print("find() was called {} times".format(find_call_count))
print("Search took {} milliseconds".format(int(time_to_find*1000)))

'''
Output
LIST IMPLEMENTATION: 
Insert took 2301 milliseconds
The size of the PhoneBook is 1000000
find() was called 1000 times
Search took 93390 milliseconds

BST IMPLEMENTATION:
Insert took 22619 milliseconds
The size of the PhoneBook is 1000000
find() was called 1000 times
Search took 18 milliseconds
'''

'''
Comments 
List: insert O(1) find O(n)
BST: insert O(logn) find O(logn)

The insert is faster for list implementation 
because we don't search for a position to place it in like the BST

The search for BST is extremely faster than the list implementation
because on average we remove half of possible inputs each time we compare
whereas with this list implementation, we must search entire list
'''
