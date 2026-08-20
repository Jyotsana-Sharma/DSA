class DoubleNode:
    def __init__(self,key,value):
        self.key = key 
        self.value = value 
        self.prev = None 
        self.next = None 
        
     

class LRUCache:

    def __init__(self,capacity):
        self.capacity = capacity 
        self.cache = {}

        self.head = DoubleNode(0,0)
        self.tail = DoubleNode(0,0)
        self.head.next= self.tail 
        self.tail.prev = self.head 
    
    def remove(self,node):
        self.node = node
        self.node.prev=self.node.next
        




    