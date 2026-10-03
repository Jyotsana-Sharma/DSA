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
        #connect left
        node.prev.next = node.next
        #connect right
        node.next.prev = node.prev
    
    def insert_at_front(self, node):
        #first save the connections of the new node 
        node.next = self.head.next
        node.prev = self.head

        #connect it from left and right both ends/nodes
        self.head.next.prev = node 
        self.head.next = node 

    def get(self, key):
        if key not in self.cache:
            return -1 
        node = self.cache[key]
        self.remove(node)
        self.insert_at_front(node)
        return node.value
    
    def put(self,key,value):
        #self.cache[key] stores the node not the value 
        if key in self.cache.keys():
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert_at_front(node)
        else:
            node = DoubleNode(key,value)
            self.cache[key] = node 
            self.insert_at_front(node)
            if(len(self.cache) > self.capacity):
                last_node = self.tail.prev 
                del self.cache[last_node.key]
                self.remove(last_node)

            


    


        




    