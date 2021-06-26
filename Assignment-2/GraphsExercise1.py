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

graph = GraphWithAdjacencyList()
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
print("size() returns {}, 3 is expected".format(graph.size()))
print()

graph.add_edge(1, 2)
graph.add_edge(1, 3)
adj_nodes = [x.data for x in graph.get_adj_nodes(1)]
print("data in adj_nodes(1) returns {}, [2, 3] is expected".format(adj_nodes))
print()

graph.remove_edge(1, 3)
adj_nodes = [x.data for x in graph.get_adj_nodes(1)]
print("data in adj_nodes(1) returns {}, [2] is expected".format(adj_nodes))
adj_nodes = [x.data for x in graph.get_adj_nodes(3)]
print("data in adj_nodes(3) returns {}, [] is expected".format(adj_nodes))
print()

graph.remove_node(2)
print("size() returns {}, 2 is expected".format(graph.size()))
adj_nodes = [x.data for x in graph.get_adj_nodes(1)]
print("data in adj_nodes(1) returns {}, [] is expected".format(adj_nodes))


