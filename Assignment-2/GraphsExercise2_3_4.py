class GraphNode:
	def __init__(self, data):
		self.data = data

class GraphWithAdjacencyList:
	def __init__(self) -> None:
		self.adj_nodes = {}

	def add_node(self, key: int) -> None:
		node = GraphNode(key)
		self.adj_nodes[node] = []

	def remove_node(self, key: int) -> None:
		for node, adj_nodes in self.adj_nodes.items():
			if node.data != key:
				continue
			for adj_node in adj_nodes: 
				self.adj_nodes[adj_node].remove(node)
			del self.adj_nodes[node]
			break

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
		self.adj_nodes[second_node].append(first_node)

	def remove_edge(self, node1: int, node2: int) -> None:
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

		self.adj_nodes[first_node].remove(second_node)
		self.adj_nodes[second_node].remove(first_node)

	def get_adj_nodes(self, key: int) -> list:
		for node, adj_nodes in self.adj_nodes.items():
			if node.data != key:
				continue
			return adj_nodes

	def size(self):
		return len(self.adj_nodes)

	def dfs(self, key: int) -> None:
		start_node = None
		for node in self.adj_nodes:
			if node.data == key:
				start_node = node
			if start_node != None:
				break

		if start_node == None:
			return None

		stack = [start_node]
		printed_nodes = []
		while len(stack) != 0: 
			key_node = stack.pop()
			if key_node in printed_nodes:
				continue
			print(key_node.data, end = ' ')
			printed_nodes.append(key_node)
			for node in self.adj_nodes[key_node]:
				stack.append(node)

	def bfs(self, key: int) -> None:
		start_node = None
		for node in self.adj_nodes:
			if node.data == key:
				start_node = node
			if start_node != None:
				break

		if start_node == None:
			return None

		queue = [start_node]
		printed_nodes = []
		while len(queue) != 0: 
			key_node = queue.pop(0)
			if key_node in printed_nodes:
				continue
			print(key_node.data, end = ' ')
			printed_nodes.append(key_node)
			for node in self.adj_nodes[key_node]:
					queue.append(node)
					


	def min_edges(self, node1: int, node2: int) -> None: 
		first_node = None
		second_node = None
		for node in self.adj_nodes:
			if node.data == node1:
				first_node = node
			elif node.data == node2:
				second_node = node
			if first_node != None and second_node != None:
				break				

		if first_node == None or second_node == None:
			return -1

		queue = [first_node]
		visited_nodes = [first_node]
		min_edges_from_1st = {first_node: 0}
		while len(queue) != 0: 
			key_node = queue.pop(0)
			for node in self.adj_nodes[key_node]:
				if node not in visited_nodes:
					queue.append(node)
					visited_nodes.append(node)
					min_edges_from_1st[node] = min_edges_from_1st[key_node] + 1
		return min_edges_from_1st[second_node]


graph = GraphWithAdjacencyList()
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)
graph.add_node(6)
graph.add_node(7)
graph.add_node(8)

graph.add_edge(1, 2) # GRAPH DIAGRAM:
graph.add_edge(1, 3) #
graph.add_edge(1, 6) # 8 - 4 - 3 - 1 - 2
graph.add_edge(6, 7) #     |       |   |   
graph.add_edge(3, 4) #     5       6   |   
graph.add_edge(4, 5) #             |   |   
graph.add_edge(4, 8) #             7---
graph.add_edge(2,7)

print("1 then (2 7 6 or 6 7 2) or (3 4 5/8 8/5) in any order")
graph.dfs(1)

print('\n')

print("1 then 2 6 3 in any order")
print("then 7 4 in any order")
print("then 8 5 in any order")
graph.bfs(1)

print('\n')

print("min_edges(1,2) returns {}, 1 expected".format(graph.min_edges(1,2)))
print("min_edges(1,7) returns {}, 2 expected".format(graph.min_edges(1,7)))
print("min_edges(2,7) returns {}, 1 expected".format(graph.min_edges(2,7)))
print("min_edges(5,7) returns {}, 5 expected".format(graph.min_edges(5,7)))


