# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers(i.e the pair) such that they add up to the given target.
# Example 1:
#   Input: [1, 2, 3, 4, 6], target=6
#   Output: [1, 3]
#   Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
# Example 2:
#   Input: [2, 5, 9, 11], target=11
#   Output: [0, 2]
#   Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

# Brute Force Approach will be is to iterate through the array, taking one number at a time and searching for the second
# number through Binary Search. Time Complexity: O(nlogn) and Space Complexity: O(1)

# Using Hash Table : Time Complexity: O(n) and Space Complexity: O(N)


def pairWithTargetSum1(nums, target):
    dic = {}
    for key,value in enumerate(nums):
        item = target - value
        if item not in dic:
            dic[value] = 1
        else:
            return [min(key, nums.index(item)), max(key, nums.index(item))]
    return [-1, -1]


# Using Two Pointer : Time Complexity: O(n) and Space Complexity: O(1)

def pairWithTargetSum(nums, target):
    left = 0
    right = len(nums)-1
    result = []
    while left < right:
        if nums[left]+nums[right] == target:
            result.append(left)
            result.append(right)
            return result
        elif nums[left]+nums[right] < target:
            left += 1
        else:
            right -= 1
    return False


# print(pairWithTargetSum1([2, 5, 9, 11], 11))