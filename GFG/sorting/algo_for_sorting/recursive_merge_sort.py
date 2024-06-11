def merge(a,l,mid,h):

    k=l
    b=[None]*len(a)
    i,j=l,mid+1
    while(i<=mid and j<=h):
        if(a[i]<a[j]):
            b[k]=a[i]
            i+=1
            k+=1
        elif(a[j]<a[i]):
            b[k]=a[j]
            j+=1
            k+=1
    
    for s in range(i,mid+1):
        b[k]=a[s]
        k+=1
    for t in range(j,h+1):
        b[k]=a[t]
        k+=1
    for i in range(l,h+1): 
        a[i]=b[i]


def recursive_merge_sort(a,l,h):
    if(l<h):
        mid = (l+h)//2
        recursive_merge_sort(a,l,mid)
        recursive_merge_sort(a,mid+1,h)
        merge(a,l,mid,h)
    
    return a


a = [int(number) for number in input().split(" ")]

recursive_merge_sort(a,0,len(a)-1)

print(f'\n sorted array post recursive merge sort : {a}\n')