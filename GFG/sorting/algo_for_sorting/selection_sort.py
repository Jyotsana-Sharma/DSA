def selection_sort(arr):
    n = len(arr)
    j = 0

    for i in range(0, n - 1):
        j = i + 1
        key_min = arr[i]
        index_ = i

        # Calculate the minimum value in the next subarray (excluding the arr[i] element)
        for k in range(j, n):
            if arr[k] < key_min:
                key_min = arr[k]
                index_ = k

        # Swapping the minimum element from the subarray with the current element
        if arr[i] > key_min:
            arr[index_] = arr[i]
            arr[i] = key_min

    return arr


def selection_sort_optimized(arr):

    n = len(arr)

    j = 0
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        if arr[i] > arr[min_index]:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = [int(number) for number in input().split(" ")]

sorted_arr = selection_sort(arr[:])
sorted_arr1 = selection_sort_optimized(arr[:])
print(f"\n sorted_arr selection sort : {sorted_arr}\n")
print(f'\n selection sort optimized : {sorted_arr1}\n')
