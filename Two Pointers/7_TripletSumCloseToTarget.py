# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target
# number as possible, return the sum of the triplet. If there are more than one suc triplet, return the sum of the triplet
# with the smallest sum.

# Example 1:
#   Input: [-2, 0, 1, 2], target=2
#   Output: 1
#   Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
# Example 2:
#   Input: [-3, -1, 1, 2], target=1
#   Output: 0
#   Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
# Example 3:
#   Input: [1, 0, 1, 1], target=100
#   Output: 3
#   Explanation: The triplet [1, 1, 1] has the closest sum to the target.


# 1. abs(target-totalsum) => minimum
# 2. totalsum => minimum
def tripletSumCloseToTarget(arr, target_sum):
    arr.sort()
    smallestDifference = float("inf")
    for i in range(len(arr)-2):
        left = i+1
        right = len(arr)-1
        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:  # We've found a triplet with an exact sum
                return target_sum - target_diff   # return sum of all the numbers

            # the second part of the following "if" is to handle the smallest sum when
            # we have more than one solution
            if abs(target_diff) < abs(smallestDifference) or (abs(target_diff) == abs(smallestDifference) and target_diff > smallestDifference) :
                smallestDifference = target_diff    # save the closest and biggest difference

            if target_diff > 0:
                left += 1          # we need a triplet with a bigger sum
            else:
                 right -= 1        # we need a triplet with a smaller sum

    return target_sum - smallestDifference


# Time complexity : O(n2) and Space Complexity : O(n)






