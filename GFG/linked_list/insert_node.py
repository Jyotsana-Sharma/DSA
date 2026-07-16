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


head = ListNode(10)
second_node = ListNode(20)
third_node = ListNode(30)

head.next = second_node
third_node.next = None 

head = insert_at_beginning(head, 100)
print(head.val)
head = insert_at_beginning(head, 200)
print(head.val)
traverse_linked_list(head)


head = insert_at_end(head, 400)
head = insert_at_end(head, 500)

traverse_linked_list(head)



