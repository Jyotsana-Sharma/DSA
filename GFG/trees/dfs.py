"""
DFS is Depth first search which we use mainly for finding the max height/depth of the tree 
example : 
       1
      /  \\
     2    3 
    / \\  / \\
   4   5  6  7

output : 3
"""

from collections import deque

class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 
        
def dfs(root):
    if root is None:
        return 0 
    
    lh = dfs(root.left)
    rh = dfs(root.right)
    return 1 +max(lh,rh)
    
   


root = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

root.left = two 
root.right = three 
two.left = four 
four.left = None 
four.right = None 
two.right = five 
five.right = None 

five.right = None 
three.left= six
three.right = seven 

six.right = None 

seven.right = None
result = dfs(root)
print(result)


