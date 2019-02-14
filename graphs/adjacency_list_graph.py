/**
  Creates a adjacency-list graph
**/

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list) 
        
    def add(self, key, value):
        self.graph[key].append(value)

    def get_graph(self):
        for node in self.graph:
            print("{0}".format(node), end="")
            for adjacency in self.graph[node]:
                print("-->{0}".format(adjacency), end="")
            print()
        

g = Graph()
g.add(1, 2)
g.add(2, 3)
g.add(1, 4)
g.add(3, 5)
g.add(3, 6)
g.get_graph()
