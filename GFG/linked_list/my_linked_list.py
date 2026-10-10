class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
  
        self.size = 0
        self.head = None
    
    def get(self,index):
        if(index<0 or index>self.size):
            return -1 
        current = self.head 
        for _ in range(index-1):
            current = current.next
        return current.val
            


    def addAtHead(self,val):
        self.addAtIndex(0,val)

    def addAtTail(self,val):
        self.addAtIndex(self.size,val)

    def addAtIndex(self,index,val):
        if(index<0 or index>self.size):
            return 
        new_node = ListNode(val)

        current = self.head 
        if(index==0):
            #since index 0 will become new head and current holds older head tadaaaa 
            new_node.next = current
            #oops donot forget to udpate the new head 
            self.head = new_node
        else:
            for _ in range(index-1):
                current = current.next
            #just for my note and understanding 
            #I have ll as 1->3 current is at 1 inserting at index 1 with value 2 ll should become 1->2->3
            #2.next should be guess ummm it should be 3 right?  
            #done new_node became 2->3 done
            new_node.next = current.next 
            #but what about 1? 1.next->new_node so 1->2->3 yipeeee
            current.next = new_node
        self.size+=1





    def deleteAtIndex(self,index):
        current = self.head 
        if index<0 or index>=self.size:
            return 
        if index==0:
            self.head = self.head.next
        else:
            for i in range(0,index-1):
                current = current.next 
            current.next = current.next.next 
        self.size-=1
        
    

#execution did on leetcode platform here just practicing again and again till I ssshhhhhh
# get(index)
# addAtHead(val)
# addAtTail(val)
# addAtIndex(index, val)
# deleteAtIndex(index)