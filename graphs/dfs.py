/**
  DFs traversal for graph
  Result: 0 1 4 2 3
**/

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list) 
        
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, s): 
        visited = [False] * (len(self.graph)) 
        self.DFS_Visit(visited, s)
        
    def DFS_Visit(self, visited, v):
        visited[v] = True
        print(v)
        for u in self.graph[v]:
            if visited[u] == False:
                self.DFS_Visit(visited, u)
                

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 4) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
g.addEdge(4, 0)
  
print("Following is DFS from (starting from vertex 0)")
g.DFS(0) 
