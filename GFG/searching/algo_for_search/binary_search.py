def recursive_binary_search(left_index,right_index,arr,search_key):
    print('\n Recursive function of Binary Search')


    middle_index = (left_index+right_index)//2

    if(arr[middle_index] == search_key):
        return middle_index
    
    elif(arr[middle_index]>search_key):
        return recursive_binary_search(left_index,middle_index-1,arr,search_key)
    
    elif(arr[middle_index]<search_key):
        return recursive_binary_search(middle_index+1,right_index,arr,search_key)
    
    return -1

def iterative_binary_search(n,arr,search_key):
    print("\n Iterative function of Binary Search")
    left_index = 0
    right_index = n
    middle_index = (left_index+right_index)//2
    while(left_index<=right_index):
        middle_element = arr[middle_index]

        #check if it is the middle element or not
        if(arr[middle_index]==search_key):
            return middle_index
        
        #check if the searched element is larger/bigger than the searched keyword that means the searched keyword lies in the left subarray
        elif(arr[middle_index]>search_key):
            right_index = middle_index-1

        elif(arr[middle_index]<search_key):
            left_index = middle_index + 1
        
        else:
            return "something is wrong here!!"


n= int(input())
#array should be sorted for binary search
arr = [int(number) for number in input().split()]
search_key = int(input())
recursive_binary_search_index=recursive_binary_search(0,n,arr,search_key)
iterative_binary_search_index = iterative_binary_search(n,arr,search_key)
print(f"\n Binary Recursive function called for key {search_key} and its index {recursive_binary_search_index}\n")
print(f"\n Binary Iterative function called for key {search_key} and its index {iterative_binary_search_index} \n")


