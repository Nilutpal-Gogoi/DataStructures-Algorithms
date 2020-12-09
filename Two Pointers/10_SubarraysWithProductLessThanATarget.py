# Given an array with positive numbers and a target number, find all of its contiguous subArrays whose product is less
# than the target number.

# Example 1:
#   Input: [2, 5, 3, 10], target=30
#   Output: [2], [5], [2, 5], [3], [5, 3], [10]
#   Explanation: There are six contiguous subarrays whose product is less than the target.
# Example 2:
#   Input: [8, 2, 6, 5], target=50
#   Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
#   Explanation: There are seven contiguous subarrays whose product is less than the target.


# Here we will use deque(Doubly ended queue) from the collections module. Deque is preferred over list in the cases
# where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time
# complexity for append and pop operations as compared to list which provides O(n) time complexity.


from collections import deque

def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while (product >= target and left < len(arr)):
            product /= arr[left]
            left += 1
# since the product of all numbers from left to right is less than the target therefore, all subarrays from left to
# right will have a product less than the target too; to avoid duplicates, we will start with a subarray containing
# only arr[right] and then extend it.
        temp_list = deque()
        for i in range(right, left-1, -1):
            temp_list.append(arr[i])
            result.append(list(temp_list))
