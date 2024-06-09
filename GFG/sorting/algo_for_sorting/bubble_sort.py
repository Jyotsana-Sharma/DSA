def bubble_optimized(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


def bubble_sort(arr):

    n=len(arr)
    j=0
    while(j<=n-1):
        for i in range(0,n-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
        j+=1
    return arr

arr = [int(n) for n in input().split(" ")]

sorted_arr = bubble_sort(arr[:])

sorted_optimized_arr = bubble_optimized(arr[:])

print(f'\n bubble optimized : {sorted_optimized_arr}\n')

print(f'\n bubble sort : {sorted_arr}\n')