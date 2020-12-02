# Given an array of unsorted numbers and a target sum, count all triplets in it such that
# arr[i]+arr[j]+arr[k] < target where i,j and k are three different indices. Write a function
# to return the count of such triplets.

# Example 1:
#   Input: [-1, 0, 2, 3], target=3
#   Output: 2
#   Explanation: There are two triplets whose sum is less than the target:
#               [-1, 0, 3], [-1, 0, 2]
# Example 2:
#   Input: [-1, 4, 2, 1, 3], target=5
#   Output: 4
#   Explanation: There are four triplets whose sum is less than the target:
#               [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]


def tripletWithSmallerSum(arr, target):
    arr.sort()
    length = 0
    if len(arr) < 3:
        return length
    for i in range(len(arr)-2):
        left = i+1
        right = len(arr)-1
        while left < right:
            if arr[i]+arr[left]+arr[right] < target:
                length += (right - left)
                left += 1
            else:
                right -= 1
    return length


print(tripletWithSmallerSum([-1, 0, 2, 3], 3))

# Time Complexity: O(n2) and Space Complexity: O(n)