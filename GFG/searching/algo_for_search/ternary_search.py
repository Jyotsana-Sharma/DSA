def iterative_ternary_search(n,arr,key):
    l = 0 
    r = n-1
    
    print(f' type : {type(l)}\n')
    print(f'type : {type(r)}\n')
    while(l<=r):
        mid1 = l+(r-l)//3
        mid2 = r - (r-l)//3
        print(f'\n l and r {l}, {r}\n')

        if(arr[mid1] == key):
            return mid1
        
        if(arr[mid2] == key):
            return mid2
        
        if(arr[mid1]>key):
            r = mid1-1
            
        
        elif(arr[mid2]<key):
            l = mid2+1
        

        else:
             l = mid1+1
             r = mid2-1

def recursive_ternary_search(n,l,r,arr,key):

    mid1 = l +(r-l)//3
    mid2 = r - (r-l)//3

    if(arr[mid1] == key):
        return mid1
    
    elif(arr[mid2] == key):
        return mid2

    elif(arr[mid1]>key):
        return recursive_ternary_search(n,l,mid1-1,arr,key)
    
    elif(arr[mid2]<key):
        return recursive_ternary_search(n,mid2+1,r,arr,key)

    else:
        return recursive_ternary_search(n,mid1+1,mid2-1,arr,key)
    

n = int(input())
arr = [int(number) for number in input().split()]
key = int(input())
l = 0 
r = n-1
searched_key_index_recursive = recursive_ternary_search(n,l,r,arr,key)
print(f'\n searched key index using recursive function : {searched_key_index_recursive}\n')
#searched_key_index_iterative = iterative_ternary_search(n,arr,key)
#print(f'\n searched key index using iterative function : {searched_key_index_iterative}\n')
