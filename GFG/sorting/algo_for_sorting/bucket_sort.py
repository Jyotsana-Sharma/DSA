
import math
def insertion_sort(arr):
    print(f'\n arr:{arr}\n')
    if(len(arr)==0):
        return []
    for i in range(1,len(arr)):
        j=i-1
        key = arr[i]
        while(j>0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

def bucket_sort(arr):
    largest_value = max(arr)
    length = len(arr)
    size = largest_value/length
    list_of_buckets = [[] for _ in range(length)]
    for i,num in enumerate(arr):
        print(num)
        num_scale = math.ceil(num/size)
        num_scale-=1
        list_of_buckets[num_scale].append(num)
    print(f'\n list of buckets: {list_of_buckets}\n')
    sorted_array=[]
    for array in range(0,len(list_of_buckets)):
        sorted_array_insertion = insertion_sort(list_of_buckets[array])
        sorted_array.append(sorted_array_insertion)
    print(f'\n sorted array : {sorted_array}\n')
    return sorted_array

        


arr = [float(number) for number in input().split(" ")]
sorted_arr = bucket_sort(arr)
print(f'\n sorted array after bucket sort algorithm: {sorted_arr}\n')
#Steps to understand the bucket sort algorithm 
#It is used to assign the elements into a bucket to be sorted
#Step 1: Calculate the largest_value from an array(0.3,0.2,0.1) largest_value=0.3
#Find the length of an array(3)
#Find the size = largest_value/length
#Step 2:Create the "length"(3) times of list in our example it would be 3
#Step 3: Divide the element by the size to find its bucket