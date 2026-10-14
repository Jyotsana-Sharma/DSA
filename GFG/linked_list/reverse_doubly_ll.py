#brute force 
def reverse_dll_brute_force(head):
    #5->3->2->1->9 
    temp = head 
    stack = []
    while temp is not None:
        stack.append(temp.val)
        temp = temp.next 
    #my stack has values as 9,1,2,3,5
    temp = head 
    #now we can traverse again and then replace the existing dll values with the stack values 
    while temp is not None:
        #in the first iteration 9 got popped e has 9 
        e = stack.pop()
        #assigned 9 to the head value of dll
        temp.val = e
        temp = temp.next 
    return head 