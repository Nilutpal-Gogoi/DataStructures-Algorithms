# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the
# duplicates in-place return the length of the subarray that has no duplicate in it.

# Example 1:
#   Input: [2, 3, 3, 3, 6, 9, 9]
#   Output: 4
#   Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
# Example 2:
#   Input: [2, 2, 2, 11]
#   Output: 2
#   Explanation: The first two elements after removing the duplicates will be [2, 11].

# The brute force approach will be by using hash table/dictionary:
# Time Complexity: O(n) and Space Complexity: O(n)


def remove_duplicate(nums):
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1
    return len(dic)


# print(remove_duplicate([2, 3, 3, 3, 6, 9, 9]))

# Better Approach: Time Complexity: O(n) and Space Complexity: O(1)


def remove_duplicate1(nums):
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    j = 1
    for i in range(1,len(nums)):
        if nums[i-1] != nums[i]:
            nums[j] = nums[i]
            j += 1
    return j
#   return nums[:j]    If asked to return the array with unique numbers


print(remove_duplicate1([0,0,1,1,1,2,2,3,3,4]))






