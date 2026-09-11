class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
        self.random = None 

def copy_nodes(head):
    if head is None:
        return None 
    
    cur = head
    mapping = {}

    #creating copying of new nodes
    while cur:
        new_node = Node(cur.value)
        mapping[cur]= new_node 
        cur = cur.next

    #now we have zero connection with the copied nodes 
    cur = head

    while cur:
        copy_node = mapping[cur]
    
        copy_node.next = mapping[cur.next] if cur.next else None
    
        copy_node.random = mapping[cur.random] if cur.random else None 
        cur = cur.next
    return mapping[head]

def traverse_linked_list(head):
    updated_ll = ""
    current = head 
    while(current):
        
        updated_ll = updated_ll +"->"+str(current.value) 
        current = current.next
    return updated_ll

head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
head.next = node1 
node1.next = node2
node2.next = node3
node3.next = None
node1.random = node3 
copy_node_head = copy_nodes(head)

copied_linked_list = traverse_linked_list(copy_node_head)
print(f'\n copied list with the random pointer:{copied_linked_list}\n')