def partition(l,r,arr):
    
    #here I am taking the rightmost element of an array as the pivot element
    pivot_element = arr[r]
    i=l-1
    for j in range(l,r):
        if(arr[j]<=pivot_element):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1


def quicksort(arr,l,r):
    n=len(arr)
    # l = 0 
    # r = n-1
    if(l<r):
        #partition element 
        pivot_element = partition(l, r, arr)
        quicksort(arr,pivot_element+1,r)
        quicksort(arr,l,pivot_element-1)

    

arr = [int(number) for number in input().split(" ")]
quicksort(arr,0,len(arr)-1)
print(f'\n arr: {arr}\n')
