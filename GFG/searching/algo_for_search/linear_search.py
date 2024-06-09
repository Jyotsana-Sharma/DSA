
def linear_search(size_of_input_array,arr,search_key):
    for index in range(0,size_of_input_array):
        if(arr[index]== search_key):
            return index

size_of_input_array = int(input())
arr= [int(number) for number in input().split()]
search_key = int(input())

searched_key_index = linear_search(size_of_input_array,arr,search_key)
print(f" Searched key's {search_key} index is {searched_key_index}")