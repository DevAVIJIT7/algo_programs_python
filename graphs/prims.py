/**
  The idea of using key values is to pick the minimum weight edge from cut. 
  The key values are used only for vertices which are not yet included in MST, 
  the key value for these vertices indicate the minimum weight edges connecting 
  them to the set of vertices included in MST.
**/
class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)]  
                    for row in range(V)]
                    
    
    def print_prims_mst(self, parent):
        total = 0
        print("Edge \tWeight")
        for i in range(1,self.V):
            total = total + self.graph[i][parent[i]]
            print(parent[i],"-",i,"\t",self.graph[i][parent[i]])
        print("Total weight{0}".format(total))
            
    def min_key(self, key, mstSet):
        min = 99999

        for v in range(self.V):
            if(key[v] < min and mstSet[v] == False):
                min = key[v]
                min_index = v
        return min_index
        
    def prim_mst(self):
        key = [99999]*self.V
        parent = [None]*self.V
        key[0] = 0
        mstSet = [False]*self.V
        
        parent[0] = -1
        
        for x in range(self.V):
            u = self.min_key(key, mstSet)
            
            mstSet[u] = True
            
            for v in range(self.V):
                if(self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]):
                    key[v] = self.graph[u][v] 
                    parent[v] = u 
                    
        self.print_prims_mst(parent)
        
g = Graph(5) 
g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
  
g.prim_mst()
  
