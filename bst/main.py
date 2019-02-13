/** 
  Directions
    1) Implement the Node class to create
    a binary search tree.  The constructor
    should initialize values 'data', 'left',
    and 'right'.
    2) Implement the 'insert' method for the
    Node class.  Insert should accept an argument
    'data', then create an insert a new node
    at the appropriate location in the tree.
    3) Implement the 'contains' method for the Node
    class.  Contains should accept a 'data' argument
    and return the Node in the tree with the same value.
    If the value isn't in the tree return null.
**/

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
    def insert(self, data):
        if self.data < data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
                
    
    def contains(self, data):
        if self.data is data:
            return self.data
            
        if (self.data < data and self.right): 
            return self.right.contains(data)
            
        if (self.data > data and self.left):
            return self.left.contains(data)

        return None

