class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_all_vals(current):
    
    while(current):
        print(current.val)
        current = current.next 

def count_no_nodes(current):
   
    node_cnt = 0 
    while(current):
        current = current.next
        node_cnt+=1
    print(f"the number of nodes : {node_cnt}")

def sum_of_all_values_of_nodes(current):
    
    res =0 
    while(current):
        res+=current.val
        current = current.next
    print(f"sum :{res}\n")

def max_val(current):
    if current is None:
        return None 
    
    max_val = current.val
    current = current.next
    while(current):
        if(max_val<current.val):
            max_val = current.val
        current = current.next
    print(f"max value :{max_val}\n")

def search_val(current,val):
    bool_val = False
    while(current):
        if(current.val==val):
            bool_val = True
        current= current.next

    print(f'value found at : {bool_val}')

def find_min(current):
    min_val = float('inf')
    while(current):
        if(current.val<min_val):
            min_val=current.val
        current = current.next
    print(f'\n min val: {min_val}\n')

def average(current):
    avg = 0 
    cnt =0 
    while(current):
        avg+=current.val
        cnt+=1
        current = current.next 
    print(f'\n average : {avg//cnt}\n')
# Create three nodes
current = ListNode(10)
second_node = ListNode(20)
third_node = ListNode(30)
current.next = second_node
second_node.next = third_node
third_node.next = None

print_all_vals(current)
count_no_nodes(current)
sum_of_all_values_of_nodes(current)
max_val(current)

search_val(current,20)
search_val(current,220)
find_min(current)
average(current)