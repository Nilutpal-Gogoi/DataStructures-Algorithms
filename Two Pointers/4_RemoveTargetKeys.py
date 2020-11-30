# Given an unsorted array of numbers and a target ‘key’, remove all instances of
# ‘key’ in-place and return the new length of the array.


def removeTarget(nums, target):
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    j = 0
    for i in range(1,len(nums)):
        if nums[j] == target and nums[i] != target:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return j


print(removeTarget([2, 11, 2, 2, 1], 2))


# Time Complexity: O(N) and Space Complexity: O(1)