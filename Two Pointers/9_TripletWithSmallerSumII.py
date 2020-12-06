# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that
# arr[i]+arr[j]+arr[k] < target where i, j and k are three different indices. Write a function to return the list of
# all such triplets instead of the count. How will the time complexity change in this case?

# Example 1:
#   Input: [-1, 0, 2, 3], target=3
#   Output: 2
#   Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
# Example 2:
#
#   Input: [-1, 4, 2, 1, 3], target=5
#   Output: 4
#   Explanation: There are four triplets whose sum is less than the target:
#    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]


# [ -1, 1, 2, 3, 4], 5

def tripletWithSmallerSum(arr, target):
    arr.sort()
    result = []
    for i in range(len(arr)-2):
        left = i+1
        right = len(arr)-1
        while left < right:
            if arr[i] + arr[left] + arr[right] < target:
                for j in range(right, left, -1):
                    result.append([arr[i], arr[left], arr[j]])
                left += 1
            else:
                right -= 1
    return result


print(tripletWithSmallerSum([-1,4,2,1,3],5))

# Time Complexity: O(n3) and space complexity: O(n)
