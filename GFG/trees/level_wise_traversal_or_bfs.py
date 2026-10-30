"""
Level wise traversal is also called BFS that is breadth first search 
here we can use the queue which operates on the FIFO first in and first out 
queue will be used to store the root and its left and right children 
stack will be used to store all the traversed elements 
example : 
       1
      /  \\
     2    3 
    / \\  / \\
   4   5  6  7

output : [[1],[2,3],[4,5],[6,7]]
      

"""

from collections import deque

class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 
        
def level_wise_traversal(root):
    if root is None:
        return []
    #to store all the traversed nodes 
    stack = []

    #to store the level wise nodes which visits 
    queue = deque()
    queue.append(root)
    
    while queue:
        length = len(queue)
    
        list_new = []
        for i in range(0,length):
            
            node = queue.popleft()
            
            if(node.left!=None):
                queue.append(node.left)
            if(node.right!=None):
                queue.append(node.right)
            list_new.append(node.val)
        stack.append(list_new)    
    return stack
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
result = level_wise_traversal(root)
print(result)


