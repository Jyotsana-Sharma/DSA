"""
    Drinks
    /     \\
   /        \\
  Hot        Cold 
  /  \\        /  \\ 
Coffee Tea   Cola Matcha

"""
#create a class node similar to linked list one except here we will be having left pointer and right pointer
class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 


#creating all the nodes 
drinks = Node("drinks")
hot = Node("hot")
cold = Node("cold")
coffee = Node("coffee")
tea = Node("tea")
cola = Node("cola")
matcha = Node("matcha")

#connecting left and right nodes now 
drinks.left = hot 
drinks.right = cold 
hot.left = coffee 
hot.right = tea 
cold.left = cola 
cold.right = matcha 
print(drinks.left.val)
print(cold.left.val)
        