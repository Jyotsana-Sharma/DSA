class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None 
        self.prev = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    #Insert at the head 
    def insert_at_head(self,val):
        new_node = Node(val)
        new_node.next = None 

        if not self.head:
            self.head = new_node 
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            new_node = self.head 

    #add at the tail/end of the doubly linked list        
    def addAttail(self,val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
        else:
            current = self.head 

            while current.next:
                current = current.next 

            current.next = new_node 
            new_node.prev = current

    #insert at index idx with value val 
    def addAtIndex(self,index,val):
        new_node = Node(val)

        if index==0:
            self.insert_at_head(val)

        else:
            current = self.head 
            i=0
            while current and i<index-1:
                current = current.next 
                i+=1
            if current is None:
                print("Position out of bounds")

        #connections done as per new_node   
        new_node.next = current.next 
        new_node.prev = current 
        
        #possibility there will be current which will point to the last node so check if the current.next is Not None and has some value 
        #then do update the address of the current node's next value's previous address which is still pointing to the current 
        if current.next:
            current.next.prev = new_node

        current.next = new_node 
    
    def delete_head_node(self):
        """
        delete_head_node function deletes the head node of the doubly linked list 
        """
        pass 

    def delete_last_node(self):
        pass 

    def delete_in_between_node(self,val,index):
        pass 
    
    def get_index(self,index):
        pass 

    def traverse(self):
        pass 




    


    