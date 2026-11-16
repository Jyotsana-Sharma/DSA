class  Node:
    def __init__(self,val):
        self.val= val 
        self.left = None 
        self.right = None 


#traversing the binary tree using preorder traversal 
def traverse_bt(node):
    result = []
    preorder_traverse(node,result)

    return result

def preorder_traverse(node,result):
    if node is None:
        result.append(0)
        return 0
    
    result.append(node.val)
    preorder_traverse(node.left,result)
    preorder_traverse(node.right,result)

def check_same_tree(p,q):
    p_res = traverse_bt(p)
    q_res = traverse_bt(q)
    print(p_res)
    print(q_res)
    if(len(p_res)!=len(q_res)):
        return False
    for i,j in zip(p_res,q_res):
        if(i!=j):
            return False 
    return True 
    

root_p = Node(1)
p_node_left = Node(2)
p_node_right = Node(3)
root_p.left = p_node_left
root_p.right = p_node_right 

root_q = Node(1)
q_node_left = Node(2)
q_node_right = Node(3)
root_q.right =  q_node_right
root_q.left =  q_node_left 

bool_res = check_same_tree(root_p,root_q)
print(bool_res)