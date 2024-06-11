def merging_single_list_sorted(arr,l,mid,h):

    k=0

    b=[None]*(h-l+1)

    i,j=l,mid+1
  
    while(i<=mid and j<=h):
        if(arr[i]<arr[j]):
            b[k]=arr[i]
            i+=1

        else:
            b[k]=arr[j]
            j+=1
        k+=1

    while(i<=mid):
        b[k]=arr[i]
        i+=1
        k+=1
    while(j<=h):
        b[k]=arr[j]
        j+=1
        k+=1
    
    for idx in range(l,h+1):
        arr[idx]=b[idx-l]
  



def iterative_merge_sort(arr):

    n=len(arr)
    p=2
    while(p<=n):
        i=0
        while(i+p-1<n):
            l=i
            h=i+p-1
            mid = (l+h)//2
            merging_single_list_sorted(arr,l,mid,h)
            i=i+p
        if(n-i>p//2):
            l=i
            h=i+p-1
            mid = (l+h)//2
            merging_single_list_sorted(arr,l,mid,n-1)
        p=p*2
   
    if(p//2<n):
        merging_single_list_sorted(arr,0,p//2 -1,n-1)

    return arr



arr= [int(number) for number in input().split(" ")]

arr=iterative_merge_sort(arr)
print(f'\n arr: {arr}\n')



''''
def merging_single_list_sorted(arr, l, mid, h):
    # Initialize temporary array to store merged result
    temp = [None] * (h - l + 1)
    i, j, k = l, mid + 1, 0  # Initialize pointers for both halves and temp array

    # Merge two halves into temp array
    while i <= mid and j <= h:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    # Copy remaining elements from left half
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements from right half
    while j <= h:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy merged elements from temp array back to original array
    for idx in range(l, h + 1):
        arr[idx] = temp[idx - l]


def iterative_merge_sort(arr):
    n = len(arr)
    p = 2

    while p <= n:
        i = 0
        while i + p - 1 < n:
            l = i
            h = i + p - 1
            mid = (l + h) // 2
            merging_single_list_sorted(arr, l, mid, h)
            i = i + p
        if n - i > p // 2:
            l = i
            h = i + p - 1
            mid = (l + h) // 2
            merging_single_list_sorted(arr, l, mid, n - 1)
        p = p * 2

    if p // 2 < n:
        merging_single_list_sorted(arr, 0, p // 2 - 1, n - 1)

    return arr

# Test the code
arr = [8, 3, 7, 4, 9, 2, 6, 5, 1]
sorted_arr = iterative_merge_sort(arr)
print("Sorted array:", sorted_arr)
'''
