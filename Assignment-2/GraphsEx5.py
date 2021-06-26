class GraphNode:
	def __init__(self, data):
		self.data = data

class DirectedGraphCourseSchedule:
	def __init__(self) -> None:
		self.adj_nodes = {}

	def add_node(self, key: int) -> None:
		node = GraphNode(key)
		self.adj_nodes[node] = []

	def add_edge(self, node1: int, node2: int)-> None:
		first_node = None
		second_node = None
		for node, adj_nodes in self.adj_nodes.items():
			if node.data == node1:
				first_node = node
			elif node.data == node2:
				second_node = node
			if second_node != None and first_node != None:
				break

		if second_node == None or first_node == None: 
			return

		self.adj_nodes[first_node].append(second_node)

	def size(self):
		return len(self.adj_nodes)

	def is_acyclic(self, key: int) -> bool:
		start_node = None
		for node in self.adj_nodes:
			if node.data == key:
				start_node = node
			if start_node != None:
				break

		stack = [start_node]
		visited_nodes = []
		while len(stack) != 0: 
			key_node = stack.pop()
			if key_node in visited_nodes:
				return True
			visited_nodes.append(key_node)
			for node in self.adj_nodes[key_node]:
				stack.append(node)
		return False

def can_finish_all_courses(num_courses: int, prereqs: list) -> bool:
	node_to_start_search = prereqs[-1][-1]
	graph = DirectedGraphCourseSchedule()
	for num in range(num_courses):
		graph.add_node(num)
	for prereq in prereqs: 
		first_node = prereq.pop()
		while len(prereq) != 0: 
			second_node = prereq.pop()
			graph.add_edge(first_node, second_node)
			first_node = second_node
	return not graph.is_acyclic(node_to_start_search) 

print(can_finish_all_courses(2, [[1, 0]])) # True
print(can_finish_all_courses(2, [[1, 0], [0,1]])) # False
print(can_finish_all_courses(5, [[3, 4, 1], [0,1], [2, 1]]))  # True
print(can_finish_all_courses(3, [[0, 1, 2], [2, 0]]))  # False
print(can_finish_all_courses(9, [[4, 5, 6, 7, 8, 9],
				[3, 2, 1],
				[2, 0]])) # True
