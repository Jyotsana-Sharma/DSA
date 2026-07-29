## Reverese a Linked List 

class ListNode:
    def __init__(self,val):
        self.val = val 
        self.next = None 

def reverse_linked_list(head):
    prev = None 
    current = head 
    
    while current:
        #saving the next node
        next_node = current.next
        #reverse the current pointer(10.next->None) 
        current.next = prev 
        # moving previous forward(<-)
        prev = current 
        #moving current forward(->)
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
    slow = current
    fast = current

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if(slow==fast):
            return True
        
    return False 

def merge_two_linked_list(list1,list2):
    dummy = ListNode(0)
    tail = dummy 

    while list1 and list2:
        if(list1.val<list2.val):
            tail.next = list1
            tail = tail.next 
            list1 = list1.next 
        else:
            tail.next = list2
            tail = tail.next
            list2 = list2.next 
        
    if list1:
        tail.next = list1
    if list2 : 
        tail.next = list2
    return dummy.next

def remove_nth_from_end(head, n):
    dummy_node = ListNode(0)
    dummy_node.next = head
    slow = dummy_node 
    fast = dummy_node 
    for i in range(n+1):
            fast = fast.next
    while fast:
        slow = slow.next 
        fast = fast.next 
         
    slow.next = slow.next.next     
    return dummy_node.next 


def palindrome_linked_list(head):
  
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next


    def reverse_list(head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


    if fast:
        # Odd length: skip the middle
        second_half_list = reverse_list(slow.next)
    else:
        # Even length: start at slow
        second_half_list = reverse_list(slow)

    current = head

    while second_half_list:
        if current.val != second_half_list.val:
            return False

        current = current.next
        second_half_list = second_half_list.next
    return True


def reorder_linked_list(head):
    #Steps for reording the linked lists are:
    #Step 1: Find the middle element using slow and fast pointer we can 
    #Step 2: Reverse the second half of the linked list we can make use of prev and next_node and current 
    #Step 3: Merge the two halves 

    slow = head 
    fast = head 

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
    def reorder_reverse_linked_list(head):
        prev = None 
        current = head 
        while current:
            next_node = current.next 
            current.next = prev 
            prev = current 
            current = next_node
        return prev

    second = slow.next 
    slow.next = None 
    second = reorder_reverse_linked_list(second)
    first = head 
    #first 1->2->3 
    #second 5->4 
    while second: 
        # order to be followed : Save -> Connect -> Move

        temp1 = first.next #(temp1 = 1.next that is 2->3)
        temp2 = second.next #(temp2 = 5.next that is 4)
        first.next = second
        second.next = temp1
        first = temp1 
        second = temp2
    return 








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


## Merge two sorted linked list
head1 = ListNode(1)
first_merge_node = ListNode(3)
second_merge_node = ListNode(5)
head1.next = first_merge_node
first_merge_node.next = second_merge_node 
second_merge_node.next = None 

head2 = ListNode(2)
first_merge_node2 = ListNode(4)
second_merge_node2 = ListNode(6)
head2.next = first_merge_node2
first_merge_node2.next = second_merge_node2
second_merge_node2.next = None 

updated_linked_list_head = merge_two_linked_list(head1,head2)

merged_linked_list = traverse_linked_list(updated_linked_list_head)
print(f'\n merged linked list : {merged_linked_list}')

## Remove Nth node from the end
n = 2
removed_node_linked_list=remove_nth_from_end(updated_linked_list_head, n)
removed_node_linked_list = traverse_linked_list(removed_node_linked_list)
print(f'\n removed nth node that is 2nd node from the end: {removed_node_linked_list}')



## Check whether the linked list is a palindrome or not 
pal_head = ListNode(10)
pal_second_node = ListNode(20)
pal_third_node = ListNode(30)
pal_fourth_node = ListNode(40)
pal_head.next = pal_second_node 
pal_second_node.next = pal_third_node 
pal_third_node.next = pal_fourth_node 
pal_fourth_node.next = None 
bool_palindrome = palindrome_linked_list(pal_head)
linkedlist = traverse_linked_list(pal_head)
print(f'\n check for palindrome the linked list is : {linkedlist}')
print(f'\n Is my linked list is a palindrome or not: {bool_palindrome}, it is')
