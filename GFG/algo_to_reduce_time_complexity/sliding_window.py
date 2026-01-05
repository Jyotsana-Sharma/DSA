#Sliding window is a technique to reduce the O(n^2) time complexity to O(n)
#In short, converting a nested loop to a single loop which in turn reduces the time complexity

#Steps to solve any problem using sliding window 
#Step 1: Decide the window size, that will define the number of elements to consider at each step
#Step 2: Begin with the initial elements within the window. Do perform the initial computations/operations.
#Step 3: Slide the window, Iterate through the data, updating the window by adding the next element and removing the leftmost one.
#Step 4: Update and Evaluate: Adjust calculations or data structures based on the new element. Evaluate if the current window meets the problem’s conditions.
#Step 5: Continue Sliding: Repeat the sliding, updating, and evaluation steps until the end of the data is reached.
#Step 6: Return Result: Return the final result or outcome based on the processed windows.
#Problem 1 solved by sliding window technqiue
#Maximum Sum Subarray of Size K
'''Given an array of positive integers and a positive number k, 
find the maximum sum of any contiguous subarray of size k.'''

def max_subarray_sum(nums,k):
    max_sum = 0
    window_sum = sum(nums[:k])
    for i in range(k,len(nums)):
        window_sum+=nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum


nums = [2,1,5,1,3,2]
window_size = 3
res = max_subarray_sum(nums,window_size)
print(f'\n max subarray sum is : {res}\n')

''' Problems where sliding window can be applied:
Maximum/Minimum Subarray Sum:
Longest Substring with K Distinct Characters:
Longest Subarray with Ones after Replacement:
Find All Anagrams in a String:
Smallest Subarray with Sum at Least K:
Maximum Consecutive Ones after Flipping Zeros:
Minimum Window Substring:
Longest Repeating Character Replacement:
Fruit Into Baskets:
Subarrays with Product Less than K:
'''

