"""
A balanced binary tree is a binary tree in which the difference in the heights of the left subtree and right subtree is not more than 1 
"""
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

    if(abs(lh-rh)>1):
        return -1
    
    if (lh==-1) or (rh==-1):
        return -1 

    return max(lh,rh)+1


def balanced_binary_tree(root):

    val = dfs(root)
    if(val<0):
        return False
    else:
        return True

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
result = balanced_binary_tree(root)
if result == True:
    print("Yes the given tree is a balanced tree")
else:
    print("No the given tree is not a balanced tree")

    

