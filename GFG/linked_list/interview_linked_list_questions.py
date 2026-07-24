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
    slow = head
    fast = head 
    
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
    return slow 

#finding the first middle node in the list 10->20->30->40->50->60 using above function of finding the middle element 
# we get the second middle element which is 40 but we want 30 which is first middle node 
# rather than starting from fast = head we'll start with the fast = head.next 

def traverse_linked_list(head):
    updated_ll = ""
    current = head 
    while(current):
        
        updated_ll = updated_ll +"->"+str(current.val) 
        current = current.next
    return updated_ll

def find_cycle(head):
    current = head
    slow = current.next 
    fast = current.next

    while fast and fast.next:
        if(slow==fast):
            return True
        slow = slow.next 
        fast = fast.next.next 
    return False 



head = ListNode(10)
second_node = ListNode(20)
third_node = ListNode(30)
fourth_node = ListNode(40)
head.next = second_node 
second_node.next = third_node 
third_node.next = fourth_node 
fourth_node.next = None 

## Reverse the linked list 
updated_head = reverse_linked_list(head)

updated_linked_list = traverse_linked_list(updated_head)
print(f'\n reversed linked list : {updated_linked_list}')


## Find the middle of the linked list 
middle_element=find_middle_element(head)
print(f'\n middle element in a linked list 10->20->30->40-> None is : {middle_element.val}\n')


## Find cycle in the linked list 
cycle_head = ListNode(100)
cycle_first_node = ListNode(200)
cycle_second_node = ListNode(300)
cycle_third_node = ListNode(400)
cycle_head.next = cycle_first_node
cycle_first_node.next = cycle_second_node
cycle_second_node.next = cycle_third_node
cycle_third_node.next = cycle_first_node

bool_has_cycle =  find_cycle(cycle_head)
print(f'\n the current linked has cycle: {bool_has_cycle}\n')

