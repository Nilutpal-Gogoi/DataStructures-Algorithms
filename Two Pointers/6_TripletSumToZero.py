# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
# Example 1:
#   Input: [-3, 0, 1, 2, -1, 1, -2]
#   Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
#   Explanation: There are four unique triplets whose sum is equal to zero.
# Example 2:
#   Input: [-5, 2, -1, -2, 3]
#   Output: [[-5, 2, 3], [-2, -1, 3]]
#   Explanation: There are two unique triplets whose sum is equal to zero.


# The brute force approach will be using three loops and continuously checking the sum
# Time Complexity: O(N3) and space complexity: O(N)

# Though an idea of binary search comes but we can't use it directly because the array
# is unsorted but we can use it after we sort the array but that will decrease the
# complexity to O(n2) as we have to use binary search inside a loop.

# Better approach using two pointers inside a loop.
def searchTriplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)-2):
        num = -arr[i]
        left = i+1
        right = len(arr)-1
        while left < right:
            current_sum = arr[left]+arr[right]
            if current_sum == num:  # Found the triplet
                triplets.append([arr[i],arr[left],arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1    # Skip same element to avoid duplicate triplets
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1   # skip same element to avoid duplicate triplets
            elif current_sum < num:
                left += 1        # We need a pair with a bigger sum
            else:
                right -= 1       # We need a pair with a smaller sum
    return triplets


print(searchTriplets([-3, -2, -1, 0, 1, 1, 2]))

# Time Complexity : O(n2) and Space Complexity: O(n)