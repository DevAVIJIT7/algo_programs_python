/**
  Creates a undirected adjacency-matrix graph
**/

class Graph:
    def __init__(self, V):
        self.graph = [[0]*V for i in range(V)]
        
    def addEdge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def get_graph(self):
        for u in range(len(self.graph)):
            print("{0}".format(u), end="")
            for v in range(len(self.graph)):
                if self.graph[u][v] is 1:
                    print("-->{0}".format(v), end="")
            print()
        

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.get_graph()
