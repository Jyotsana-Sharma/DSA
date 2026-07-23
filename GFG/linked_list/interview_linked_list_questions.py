## Reverese a Linked List 

class ListNode:
    def __init__(self,val):
        self.val = val 
        self.next = None 

def reverse_linked_list(head):
    prev = None 
    current = head 
    
    while current:
        next_node = current.next 
        current.next = prev 
        prev = current 
        current = next_node

    return prev 


def find_middle_element(head):
    
    pass 

def traverse_linked_list(head):
    updated_ll = ""
    current = head 
    while(current):
        
        updated_ll = updated_ll +"->"+str(current.val) 
        current = current.next
    return updated_ll


head = ListNode(10)
second_node = ListNode(20)
third_node = ListNode(30)
fourth_node = ListNode(40)
head.next = second_node 
second_node.next = third_node 
third_node.next = fourth_node 
fourth_node.next = None 

updated_head = reverse_linked_list(head)

updated_linked_list = traverse_linked_list(updated_head)
print(f'\n reversed linked list : {updated_linked_list}')


## Find the middle of the linked list 

