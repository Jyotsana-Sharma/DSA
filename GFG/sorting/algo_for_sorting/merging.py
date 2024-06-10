### Merging two sorted lists into one list ###

def merging_two_sorted_list(a,b,m,n):
    i=0
    j=0
    c=[None]*(m+n)
    k=0
    while(i<m and j<n):
        if(a[i]>b[j]):
            c[k]=b[j]
            k+=1
            j+=1
        elif(a[i]<b[j]):
            c[k]=a[i]
            k+=1
            i+=1
    
    for s in range(i,len(a)):
        c[k]=a[s]
        k+=1
    for t in range(j,len(b)):
        c[k]=b[t]
        k+=1

    return c



### Given an array we have to sort that array using merging technique ###
### Approach : Divide an array into two half , calculate mid element and then compare each element of two subarrays and append the min element into second new array of same size ###

def merging_single_list_sorted(arr):
    l=0
    k=0
    h=len(arr)
    b=[None]*len(arr)
    mid = (l+h)//2
    i,j=l,mid+1
    while(i<=mid and j<h):
        if(arr[i]<arr[j]):
            b[k]=arr[i]
            i+=1
            k+=1
        elif(arr[j]<arr[i]):
            b[k]=arr[j]
            j+=1
            k+=1
    
    for s in range(i,mid+1):
        b[k]=arr[s]
        k+=1
    for t in range(j,h+1):
        b[k]=arr[t]
        k+=1
    
    for i in range(0,len(b)):
        arr[i]=b[i]
    return  arr

a = [int(number) for number in input().split(" ")]
b = [int(number) for number in input().split(" ")]
m = len(a)
n = len(b)

sorted_list_merged_two_list = merging_two_sorted_list(a,b,m,n)
print(f' sorted list merged two list :{sorted_list_merged_two_list}')

arr = [int(number) for number in input().split(" ")]
sorted_list_merge_one_list = merging_single_list_sorted(arr)
print(f'\n sorted merge list one array : {sorted_list_merge_one_list}\n')

