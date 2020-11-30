# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

# The brute force approach will be by using squaring all the inputs of the array and then sorting them using sort
# Time Complexity: O(nlogn) and Space Complexity: O(1)


def make_squares(arr):
    for i in range(len(arr)):
        arr[i] = arr[i]*arr[i]
    return sorted(arr)

# The better approach will be by finding the first non-negative number then using two pointers to insert the squares of
# the numbers in an array
# Time Complexity: O(n) and Space Complexity: O(1)


def make_squares1(arr):
    pointer = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            pointer = i
            break
    left = pointer - 1
    right = pointer
    squares = []
    while left >= 0 and right < len(arr):
        if(arr[left]**2) < (arr[right]**2):
            squares.append(arr[left] ** 2)
            left -= 1
        else:
            squares.append(arr[right]**2)
            right += 1
    if left < 0:
        while right < len(arr):
            squares.append(arr[right]**2)
            right += 1
    elif right == len(arr):
        while left >= 0:
            squares.append(arr[left]**2)
            left -= 1
    return squares

# print(make_squares1([-3, -1, 0, 1, 2]))

# We can also use another approach with two pointers. Here we can use two pointer from both the ends and check the
# larger one. If one is larger then it is inserted to the result array
# Time Complexity: O(n) and Space Complexity: O(1)


def make_squares2(arr):
    square = [0 for x in range(len(arr))]
    highestPointer = len(arr) - 1
    left, right = 0, len(arr)-1
    while left < right:
        leftsquare = (arr[left]**2)
        rightsquare = (arr[right]**2)
        if leftsquare > rightsquare:
            square[highestPointer] = leftsquare
            highestPointer -= 1
            left += 1
        else:
            square[highestPointer] = rightsquare
            highestPointer -= 1
            right -= 1
    return square


print(make_squares2([-3, -1, 0, 1, 2]))


