def my_approach_count_sort(a,n):
    max_ele = max(a)
    b = [0]*(max_ele+1)
    k=0
    # for i in range(0,n):
    #     for j in range(0,len(b)):
    #         if(j==a[i]):
    #             b[j]+=1
    
    for i in a:
        b[i]+=1

    for i in range(0,len(b)):
        while(b[i]>0):
            a[k]=i
            b[i]-=1
            k+=1
        
    return a

def optimized_count_sort(a,n):
    
    return ""

a = [int(number) for number in input().split(" ")]
n=len(a)
a = my_approach_count_sort(a,n)
print(f'\n count sort : {a}\n')