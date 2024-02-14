# Create a simple adjacency matrix for an undirected graph 
class Graph:
  def __init__(self, vertices):
    self.vertices = vertices
    self.graph = [[0] * vertices for _ in range(vertices)]
  
  def add_edge(self, source, destination):
    #For an undirected graph, mark both cells as 1
    self.graph[source][destination] = 1
    self.graph[destination][source] = 1

  def display(self):
    for row in self.graph:
      print(" ".join(map(str, row))) 

graph  = Graph(4)

#Add edges
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

# Display the adjacency matrix
graph.display()