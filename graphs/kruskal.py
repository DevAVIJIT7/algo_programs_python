/**
  The algorithm is a Greedy Algorithm. 
  The Greedy Choice is to pick the smallest weight 
  edge that does not cause a cycle in the MST constructed so far.
**/
from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = []
        
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
        
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        # If ranks are same, then make one as root  
        # and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
            
    def kruskal_min_spanning_tree(self):
        result = []
        parent = []
        rank = []
        i = 0
        e = 0
        
        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            
        while e < self.V - 1:
            u,v,w = self.graph[i]
            i = i + 1
            
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            if x != y:
                e = e + 1
                result.append([u,v,w])
                self.union(parent, rank, x, y)
                
        print("Following are the edges in the constructed MST")
        total = 0
        for u,v,weight  in result:
            total = total + weight
            print ("%d -- %d == %d" % (u,v,weight))
        print("Total weight {0}".format(total))
        
        
g = Graph(4) 
g.add_edge(0, 1, 10) 
g.add_edge(0, 2, 6) 
g.add_edge(0, 3, 5) 
g.add_edge(1, 3, 15) 
g.add_edge(2, 3, 4) 
  
g.kruskal_min_spanning_tree()
