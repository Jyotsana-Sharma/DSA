### Missing and repeating number ###

def my_approach(arr):
    n=len(arr)
    max_no= max(arr)
    

    ## method 1 for checking missing number
    for i in range(1,max_no):
        if(i not in arr):
            missing_no =i
            break

   

    ## Repeating number 
    arr.sort()
    i,j=0,1
    while(j<len(arr)):
        if(arr[i]==arr[j]):
            repeating_no = arr[j]
            break
        else:
            i+=1
            j+=1
    return missing_no,repeating_no,


def gfg_approach1(arr):
    a = sorted(arr)
    missing_no = 0 
    repeating_no = 0
    j=1
    for i in range(1,max(arr)):
        if(i not in a):
            missing_no = i
        if(i == arr[j]):
            repeating_no = arr[j]
        else:
            j+=1
    return missing_no,repeating_no


def gfg_approach2(arr):
    return ""

    

arr=[int(n) for n in input().split()]
missing_no,repeating_no = my_approach(arr)
missing_no, repeating_no = gfg_approach1(arr)
print(f'\n missing no and repeating no : {missing_no} and {repeating_no} \n ')
print(f'\n gfg_approach1 mIssing no: {missing_no} and repeating no : {repeating_no}\n')