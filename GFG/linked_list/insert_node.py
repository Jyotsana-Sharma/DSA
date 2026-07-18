#Insertion of a node at the beginning 

class ListNode:
    def __init__(self,val):
        self.val = val 
        self.next = None 

def insert_at_beginning(head, value):
    #creating a node for the new value to be inserted in a linked list
    new_node = ListNode(value)
    new_node.next = head 
    head = new_node
    return head 

def insert_at_end(head, value):
    current = head
    new_node = ListNode(value)
    while current.next:
        current = current.next
    
    current.next = new_node
    return head

def traverse_linked_list(head):
    str_print=""
    while(head):
        str_print=str_print +"->"+str(head.val) 
        head = head.next 
    print(str_print)

def insert_at_specific_idx(head,val,position):
    new_node = ListNode(val)
  
    if position == 0:
        new_node.next = head 
        return new_node
    current  = head

    #loop through all the elements till the position-1 i will go from 0 till 2 and will stop at idx 1
    for i in range(position-1):
        current = current.next
    
    if current is None:
        return head
    
    #we have current pointer pointing to index 1 
    #we will save the rest of the linked list to the new node's next 
    new_node.next = current.next

    #Current index 1 holds value of 100 so it's next value should be 25
    current.next = new_node 
    return head    


head = ListNode(10)
second_node = ListNode(20)
third_node = ListNode(30)

head.next = second_node
third_node.next = None 

head = insert_at_beginning(head, 100)
print(head.val) #Prints 100
head = insert_at_beginning(head, 200)
print(head.val) #Prints 200
traverse_linked_list(head) #Prints (->200->100->10->20)


head = insert_at_end(head, 400)
head = insert_at_end(head, 500)

traverse_linked_list(head) #Prints (->200->100->10->20->400->500)

insert_val = 25 
insert_val_idx = 2
insert_at_specific_idx(head,insert_val,insert_val_idx)
traverse_linked_list(head) # Prints (->200->100->10->25->20->400->500)



