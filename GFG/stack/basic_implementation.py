#Basic implementation of stack using the list 
#Initializing a class named as Stack to perform all the operations of Stack data structure
#Stack operations are pop, push, isEmpty, seek, peek all operations take O(1) time complexity.

class Stack:
    def __init__(self):
        self.stack_items = []
    
    #isEmpty operation is to check whether the stack is empty or not
    def isEmpty(self):
        return self.stack_items==[]
    
    #Push operation is to add a new element in the stack, always adds at the top of the stack
    #Assuming that the top element is at the end of the list 
    def push(self,item):
        return self.stack_items.append(item)

    #Removes the top item from the stack , It follows the LIFO rule last in first out
    def pop(self):
        return self.stack_items.pop()
    
    #Returns the top element of the stack
    def peek(self):
        return self.stack_items[len(self.stack_items)-1]
    
    #Returns the size of the stack 
    def size(self):
        return len(self.stack_items)
    
s = Stack()

print(f'\n stack empty operation: {s.isEmpty()}')
print(f'\n stack insertion operation : {s.push(2)}')
print(f'\n stack insertion operation : {s.push(3)}')
print(f'\n stack deletion operation pip : {s.pop()}')
print(f'\n stack size check : {s.size()}')
print(f'\n stack fetch last element which is our top element since we assumed the last element is top one: {s.peek()}')

    
