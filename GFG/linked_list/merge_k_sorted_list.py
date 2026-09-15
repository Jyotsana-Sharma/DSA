class Node:
    def __init__(self,head):
        self.head = None 
        self.next = None 
        self.value = None

def merge_two_list(l1,l2):
    dummy_node = Node(0)
    dummy_node.next = None
    tail = dummy_node
    while l1 and l2:
        if(l1.value > l2.value):
            tail.next = l2 
            tail = tail.next
            l2 = l2.next 
        else:
            tail.next = l1 
            tail = tail.next 
            l1 = l1.next     
    if l1: 
        tail.next = l1 
    if l2: 
        tail.next = l2 

    return dummy_node.next

def merge_multiple_list(lists):
    merged_lists = []

    for i in range(0, len(lists), 2):
        if i+1<len(lists):
            # merge two lists
            merged = merge_two_list(lists[i],lists[i+1])
            merged_lists.append(merged)
        else:
            # just carry the last list forward
            # merged = merge_two_list(merged,lists[i])
            merged_lists.append(lists[i])
    return merged_lists

def merge_lists(lists):
    if len(lists) == 0 :
        return None 
    while(len(lists)>1):
        lists = merge_multiple_list(lists)
    return lists[0] 


l1_head = Node(1)
l1_node1 = Node(4)
l1_node2 = Node(5)

l2_head = Node(1)
l2_node1 = Node(3)
l2_node2 = Node(4)

l3_head = Node(2)
l3_node1 = Node(6)

l1_head.next = l1_node1
l1_node1.next = l1_node2
l1_node2.next = None 

l2_head.next = l2_node1
l2_node1.next = l2_node2
l2_node2.next = None 

l3_head.next = l3_node1
l3_node1.next = None 

k = input("Enter the number of k linked list: ")


