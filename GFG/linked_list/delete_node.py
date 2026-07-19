class ListNode:
    def __init__(self,val):
        self.val = val 
        self.next = None

def delete_first_node(current):

    if current is None:
        return None 
    
    while current:
        current = current.next 
        break
    
    return current
    

def traverse_linked_list(head):
    str_print=""
    while(head):
        str_print=str_print +"->"+str(head.val) 
        head = head.next 
    print(str_print)




current = ListNode(10)
second_node = ListNode(20)
third_node = ListNode(30)
fourth_node = ListNode(40)

current.next = second_node 
second_node.next = third_node 
third_node.next = fourth_node 
fourth_node.next = None 
traverse_linked_list(current)
current = delete_first_node(current)
traverse_linked_list(current)

