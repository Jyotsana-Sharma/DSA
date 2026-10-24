"""
There are mainly three types of traversal in the binary trees which are following: 
1. Inorder Traversal (Left -> Root -> Right) 
2. Pre-Order Traversal (Root-> Left -> Right)
3. Post-Order Traversal (Left -> Right -> Root)
Example tree which I am going to use for all types of traversals are: 
        1
      /  \\
     2    3 
    / \\  / \\
   4   5  6  7
      /  /  /
     8   9  10

Inorder Traversal => 4 -> 2 -> 8 -> 5 -> 1 -> 9 -> 6 -> 3 -> 10 -> 7 
Preorder Traversal => 1 -> 2 -> 4 -> 5 -> 8 -> 3 -> 6 -> 9 -> 7 -> 10 
Postorder Traversal => 4 -> 5 -> 8 -> 2 -> 9 -> 6 -> 10 -> 7 -> 3 -> 1
"""


#creating a tree first 
class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None

#recursive approach of the in order traversal 
def traverse_inorder_tree(root,result):
    
    if root == None:
        return 
   
    traverse_inorder_tree(root.left,result)
    result.append(root.val)
    traverse_inorder_tree(root.right,result)

def recursive_inroder_traversal(root):
    result = []
    traverse_inorder_tree(root,result)
    return result 

#Implementation of the Inorder traversal using iterative approach
def inorder_using_stack(root):
    result = []
    current_node = root
    stack_list = []
    while current_node or stack_list:
        while current_node: 
            #append the current node to the stack list
            stack_list.append(current_node)
            #move the current node to the left 
            current_node = current_node.left
        #in case there is no left node available 
        #then we have all the leftmost node starting from the root node in the stack_list 
        #lets pop each of them and append it in the result one 
        current_node = stack_list.pop()
        result.append(current_node.val)

        #moving to the right tree now the current node points to the first node that we added in the stack_list 
        current_node = current_node.right 
    return result 
        

root = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)
ten = Node(10)
root.left = two 
root.right = three 
two.left = four 
four.left = None 
four.right = None 
two.right = five 
five.right = None 
five.left = eight 
five.right = None 
three.left= six
three.right = seven 
six.left = nine 
six.right = None 
seven.left = ten 
seven.right = None

final_inorder_binary_tree_result = recursive_inroder_traversal(root)
print(final_inorder_binary_tree_result)

iterative_inorder = inorder_using_stack(root)
print(f'\n iterative inorder: {iterative_inorder}')





