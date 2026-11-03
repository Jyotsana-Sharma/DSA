"""
Diameter of a binary tree is defined as the longest pathg between any 2 nodes 
also note that path doesnt need to pass via the root node
"""

"""Brute force approach is to get the max of left subtree and 
right subtree and then add the left height and 
right height and maintain the maxi variable which keeps track of the maximum height sum

example : 
       1
      /  \\
     2    3 
    / \\  / \\
   4   5  6  7
         /
        8
"""

class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None

maxi= 0 

def find_max(root):
    global maxi
    if root is None:
        return None 
    lh = find_height(root.left)
    rh = find_height(root.right)
    """
    reason why am I adding here lh+rh+2 
    because my find_height function uses -1 as the base case for None, 
    lh and rh only give you the edge counts inside the left and right subtrees.

    Adding + 2 bridges the gap, explicitly counting the two edges connecting the left child 
    and right child up to the current root node.
    """
    maxi = max(maxi,lh+rh+2)
    find_max(root.left)
    find_max(root.right)
    return maxi



def find_height(root):
    if root is None:
        return -1
    
    lh = find_height(root.left)
    rh = find_height(root.right)
    return max(lh,rh)+1


#another approach 
def height(root,max_diameter):
    if root is None:
        return 0

    lh = height(root.left,max_diameter[0])
    rh = height(root.right,max_diameter[0])
    max_diameter[0] = max(max_diameter[0], lh + rh)
    return 1 + max(lh,rh)

def diameter_bt(root):
    max_diameter = [0]
    diameter=height(root,max_diameter)
    return diameter
    

root = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)

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

seven.right = eight 
eight.left = None 
eight.right = None 
#uncomment below code just to check the left subtree max height and right subtree max height
# lh = find_height(root.left)
# rh = find_height(root.right)
# print(lh)
# print(rh)
maxi = find_max(root)

print(maxi)

res = diameter_bt(root)
print(res)

