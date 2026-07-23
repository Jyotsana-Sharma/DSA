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

def delete_last_node(head):
    #always traverse current and keep head unchanged 
    if head is None:
        return None
     
    if head.next is None:
        return None 
    prev = None 
    current = head

    while current.next:
        prev = current
        current = current.next
    prev.next = None 
    return head 

def delete_at_position(head, position):
    prev = None 
    current = head 
    if(position==0):
        return current.next
    
    else:
        #i will go from 0 till 1 
        for i in range(position):
            prev = current
            current = current.next
         
        prev.next = current.next
        return head




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
# current = delete_first_node(current)
traverse_linked_list(current)

# current = delete_last_node(current)
traverse_linked_list(current)

#delete at specific position
# position = 0 
position = 2
current = delete_at_position(current,position)
traverse_linked_list(current)