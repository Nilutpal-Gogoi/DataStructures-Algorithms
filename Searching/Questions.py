# Linear Search - Whenever the order of the array given is unsorted and we have to find an element. Then we have to
# Linear search.


def UnOrderedLinearSearch(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1  # T.C - O(n) and S.C - O(1)


# Sorted/Ordered Search - If the elements of the array is already sorted.


def OrderedLinearSearch(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
        elif arr[i] > value:
            return -1
    return -1  # T.C - O(n) and S.C - O(1)


# Binary Search -


def BinarySearchIterative(arr, value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def BinarySearchRecursive(arr, value, low, high):
    if low > high:
        return False
    else:
        mid = low + (high - low) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            return BinarySearchRecursive(arr, value, mid + 1, high)
        else:
            return BinarySearchRecursive(arr, value, low, mid - 1)


# Time complexity : O(logn) , Space Complexity: O(1) [for iterative], O(logn) [for recursive]

# ---------------------------------------------------------------------------------------------------------
# QUESTION 1: Given an array of n numbers, give an algorithm for checking whether there are any
# duplicate elements in the array?


def CheckDuplicateBruteForce(arr):  # T.C O(n2) , S.C - O(1)
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] == arr[i]:
                print("Duplicate does exist")
                return arr[i]
    print("Duplicate doesn't exist")


def CheckDuplicateSorting(arr):  # T.C O(nlogn) , S.C - O(1)
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i + 1] == arr[i]:
            return True
    return False


def CheckDuplicateHash(arr):  # T.C O(n) , S.C - O(n)
    temp = {}
    for i in arr:
        if i in temp:
            return True
        else:
            temp[i] = 1
    return False


def CheckDuplicateEfficient(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])] < 0:
            print("duplicate number is ", abs(arr[i]))
            return
        else:
            arr[arr[i]] = -arr[arr[i]]
    print("There are no duplicates")


# print(CheckDuplicateEfficient([3, 2, 1, 2, 2, 3]))


# --------------------------------------------------------------------------------------------------------------
# QUESTION 2: Given an array of n numbers. Give an algorithm for finding the element which appears maximum numbers
#  of times in the array.


def MaxAppearanceBruteForce(arr):  # T.C O(n2) , S.C - O(1)
    count, max_count = 0, 0
    element = 0
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[j] == arr[i]:
                count += 1
        if count > max_count:
            max_count = count
            element = arr[i]
    return [element, max_count]


def MaxAppearanceSorting(arr):  # T.C O(nlogn) , S.C - O(1)
    arr.sort()
    count, max_count = 1, 0
    element = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            element = arr[i - 1]
    return [element, max_count]


def MaxAppearanceHash(arr):  # T.C O(n) , S.C - O(n)
    temp = {}
    max_element = 0
    for i in range(len(arr)):
        if arr[i] in temp:
            temp[arr[i]] += 1
        else:
            temp[arr[i]] = 1
    _max = 0
    for i in arr:
        if temp[i] > _max:
            _max = temp[i]
            max_element = i
    return [max_element, _max]


def MaxAppearanceEfficient(arr):  # T.C O(n) , S.C - O(1)
    n = len(arr)
    _max = 0
    maxIndex = 0
    for i in range(len(arr)):
        arr[arr[i] % n] += n
    print(arr)
    for i in range(len(arr)):
        if arr[i] // n > _max:
            _max = arr[i] // n
            maxIndex = i
    return [maxIndex, _max]


# This solution will work only if the  array element are positive and is in the range (0,n-1)
# print(MaxAppearanceEfficient([3, 2, 1, 2, 2, 3, 3, 4, 3]))


# ----------------------------------------------------------------------------------------------------------------------
# QUESTION 3: Given an array of n numbers, give an algorithm for finding the first element in the array which is
# repeated. For example, in the array A=[3, 2, 1, 2, 2, 3], the first repeated number is 3(not 2). That means, we need
# to return the first element among the repeated elements.


def firstRepeatedBrute(arr):  # T.C : O(n2) , S.C: O(1)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] == arr[i]:
                return arr[i]
    return None


# In this problem if we use sorting then the position of the elements will change and a wrong answer will be output.

# Similarly simple hashing technique can't be used


def firstRepeatedHash(arr):  # T.C : O(n) , S.C: O(n)
    table = {}
    _max = 0
    for i in range(len(arr)):
        if arr[i] not in table:
            table[arr[i]] = i + 1
        else:
            if table[arr[i]] < 0:
                continue
            else:
                num = table[arr[i]]
                table[arr[i]] = -num
    lis = []
    for value in table.values():
        if value < 0:
            lis.append(value)
    value = max(lis)
    for key, values in table.items():
        if values == value:
            return key


# print(firstRepeatedHash([3,2,1,1,2,1,2,5,5]))

# ---------------------------------------------------------------------------------------------------------------------
# QUESTION 4: FIND THE MISSING NUMBER: We are given a list of n-1 integers and these integers are in the range of 1 to n.
# There are no duplicates in the list. One of the integers is missing in the list. Given an algorithm to find the missing
# integer. EXAMPLE: i/p [1,2,4,6,3,7,8] o/p: 5


def FindMissingNumberBrute(arr):  # T.C : O(n2) , S.C: O(1)
    num = len(arr)
    for i in range(1, num + 1):
        found = 0
        for j in arr:
            if j == i:
                found = 1
        if found == 0:
            return i


# We can use sorting technique which will sort the elements in increasing order and with another scan we can find the
# missing number.   # T.C : O(nlogn) , S.C: O(1)


def FindMissingNumberSum(arr):  # T.C : O(n) , S.C: O(1)
    num = len(arr) + 1
    total = (num * (num + 1)) // 2
    amount = sum(arr)
    return total - amount


# If the sum of the numbers goes beyond the maximum allowed integer, then there can be integer overflow and we may not
# get the correct answer. We can solve this problem using XOR


def FindMissingNumberXOR(arr):  # T.C : O(n) , S.C: O(1)
    n = len(arr)
    X = 0
    for i in range(1, n + 2):
        X = X ^ i
    for i in arr:
        X = X ^ i
    return X


# print(FindMissingNumberXOR([8,2,1,4,6,5,7,9]))


# ---------------------------------------------------------------------------------------------------------------------
# QUESTION 5: Find the Number Occurring an Odd Number of Times: Given an array of postitive integers, all numbers occur
# an even number of times except one number which occurs an odd number of times. Find the number in O(n) time & constant
# space.

def findOddXOR(arr):  # T.C : O(n) , S.C: O(1)
    X = 0
    for i in arr:
        X = X ^ i
    return X


# print(findOddXOR([1,2,3,2,3,1,3]))


# --------------------------------------------------------------------------------------------------------------------
# QUESTION 6: Find The Two Repeating Elements In A Given Array: Given an array with size, all elements of the array are
# in range 1 to n and also all elements occur only once except two numbers which occur twice. Find those two repeating
# numbers. For example: if they array is 4,2,4,5,2,3,1 with size = 7 and n =5. This input has n+2 =7 elements with all
# elements occurring once except 2 and 4 which occur twice. So the output should be 4 2.


def PrintTwoRepeatedElementsBruteForce(arr):  # T.C : O(n2) , S.C: O(1)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] == arr[i]:
                print(arr[i])


# This can also be solved using sorting, after sorting we have to just check if the continuous number is same or not.
# T.C : O(nlogn) , S.C: O(1)

# Can also be solved using Hash Table. # T.C : O(n) , S.C: O(n)

# The approach is same for two missing and two repeated numbers


def PrintTwoRepeatedElementsXOR(arr):  # T.C : O(n) , S.C: O(1)
    XOR = arr[0]
    X, Y = 0, 0
    n = len(arr) - 2
    for i in range(1, len(arr)):
        XOR ^= arr[i]
    for i in range(1, n + 1):
        XOR ^= i
    rightMostSetBitNo = XOR & -(XOR - 1)
    for i in range(len(arr)):
        if arr[i] & rightMostSetBitNo:
            X = X ^ arr[i]
        else:
            Y = Y ^ arr[i]
    for i in range(1, n + 1):
        if i & rightMostSetBitNo:
            X = X ^ i
        else:
            Y = Y ^ i
    print(X, Y)


def PrintTwoRepeatedElementsNegation(arr):  # T.C : O(n) , S.C: O(1)
    lis = [0] * len(arr)
    for i in arr:
        lis[i - 1] += 1
    for i in range(len(lis)):
        if lis[i] == 2:
            print(i + 1)


# PrintTwoRepeatedElementsNegation([4,2,4,5,2,3,1])

# ----------------------------------------------------------------------------------------------------------------------
# QUESTION 7: Given an array of n elements. Find two elements in the array such that their sum is equal to given
# element K.

# With brute force approach we will use two loops in second loop we will find an element which is equal to K-arr[i]. If
# we find that element then we'll print True or we'll print the two elements.
# # T.C : O(n2) , S.C: O(1)

def twoElementsWithSumKSorting(arr, K):  # T.C : O(nlogn) , S.C: O(1)
    arr.sort()
    low = 0
    high = len(arr) - 1
    while low < high:
        if arr[low] + arr[high] == K:
            return arr[low], arr[high]
        elif arr[low] + arr[high] > K:
            high -= 1
        else:
            low += 1
    return False


# Here if the array is already sorted then the T.C is O(n)


# print(twoElementsWithSumKSorting([1,4,45,6,10,-8], 11))


# ----------------------------------------------------------------------------------------------------------------------
# QUESTION 8: Given an array A of n elements. Find three indices i,j and k such that A[i]^2 + A[j]^2 = A[k]^2 ?

def threeIndices(arr):  # T.C : O(n2) , S.C: O(1)
    arr.sort()
    for i in range(len(arr) - 2):
        j = i + 1
        k = len(arr)
        while j < k:
            if arr[i] ^ 2 + arr[j] ^ 2 == arr[k] ^ 2:
                return i, j, k
            elif arr[i] ^ 2 + arr[j] ^ 2 > arr[k] ^ 2:
                k -= 1
            else:
                j += 1
        return False


# ---------------------------------------------------------------------------------------------------------------------
# QUESTION 9: Two Elements Whose Sum Is Closest To Zero: Given an array with both positive and negative numbers, find
# the two elements such that their sum is closest to zero. For the below array, algorithm should give - 80 and 85.
# Example: [1, 60, -10, 70, -80, 85].


def twoElementsClosestToZeroBruteForce(arr):  # T.C : O(n2) , S.C: O(1)
    if len(arr) < 2:
        return False
    min_ele = 0
    max_ele = 0
    _sum = float('inf')
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] + arr[j]) < _sum:
                min_ele = min(arr[i], arr[j])
                max_ele = max(arr[i], arr[j])
    return min_ele, max_ele


def twoElementsClosestToZeroSorting(arr):  # T.C : O(nlogn) , S.C: O(1)
    arr.sort()
    if len(arr) < 2:
        return False
    low = 0
    high = len(arr) - 1
    minLeft = 1
    minRight = len(arr) - 1
    minSum = float('inf')
    while low < high:
        _sum = arr[low] + arr[high]
        if abs(minSum) > abs(_sum):
            minSum = _sum
            minLeft = low
            minRight = high
        if _sum < 0:
            low += 1
        else:
            high -= 1
    return arr[minLeft], arr[minRight]


# print(twoElementsClosestToZeroSorting([1, 60, -10, 70, -80, 85]))
# print(twoElementsClosestToZeroSorting([10, 8, 3, 5, -9, -7, 6]))

# ----------------------------------------------------------------------------------------------------------------------
# QUESTION 10: Given an array of n elements. Find three elements in the array such that their sum is equal to given
# elements K?

# The brute force solution will involve using three loops leading to O(n3) time complexity and O(1) space complexity.


def findThreeElementsSorting(arr, K):  # T.C : O(n2) , S.C: O(1)
    arr.sort()
    if len(arr) < 3:
        return False
    for i in range(len(arr)):
        low = i + 1
        high = len(arr) - 1
        req = K - arr[i]
        while low < high:
            if arr[low] + arr[high] == req:
                return arr[i], arr[low], arr[high]
            elif arr[low] + arr[high] > req:
                high -= 1
            else:
                low += 1
    return False


# Using hash will also lead to O(n2) time complexity but the space complexity will be O(n). So its not so efficient.
# print(findThreeElements([1, 6, 45, 4, 10, 18], 73))


# ---------------------------------------------------------------------------------------------------------------------
# QUESTION 11: Given an array of n integers, the 3-sum problem is to find three integers whose sum is closest to zero.

# The brute force solution will be using three loops and defining a variable which stores the sum and compares every time
# with the three elements.     # T.C : O(n3) , S.C: O(1)

def threeSumProblemSort(arr):
    arr.sort()
    if len(arr) < 3:
        return False
    num1 = 0
    num2 = 0
    num3 = 0
    min_sum = float('inf')
    for i in range(len(arr)):
        num1 = arr[i]
        low = i + 1
        high = len(arr) - 1
        _sum = arr[low] + arr[high] + arr[i]
        while low < high:
            if abs(_sum) < abs(min_sum):
                num2 = arr[low]
                num3 = arr[high]
                min_sum = abs(_sum)
            if _sum > 0:
                high -= 1
            else:
                low += 1
    return num1, num2, num3


# ---------------------------------------------------------------------------------------------------------------------
# QUESTION 12: Given a sorted array A of n elements, possibly with duplicates. Find the index of the first occurrence of
# a number in O(logn) time.

# The brute force approach will be solved using loop. For every element in the first loop we will loop again and check
# it the array. If we find then we will return the index of the element in first loop. Time complexity will be O(n2).

# arr = [2,4,10,10,10,18,20] . Here the result will be index 2.


def firstOccurrenceBinarySearch(arr, k):  # T.C : O(logn) , S.C: O(1)
    low = 0
    high = len(arr) - 1
    res = 0
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            res = mid
            high = mid - 1  # To check the left half of the mid as we have to find the first occurrence.
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return res


# print(firstOccurrenceBinarySearch([2,4,10,10,10,18,20], 10))
# ----------------------------------------------------------------------------------------------------------------------
# QUESTION 13: Given a sorted array A of n elements, possibly with duplicates. Find the index of the last occurrence of
# a number in O(logn) time.

# The brute force approach will be solved using loop. For every element in the first loop we will loop again and check
# it the array and whenever we found the element we will store the index in a variable. Later we will output the updated
# stored result. Time complexity will be O(n2).

# arr = [2,4,10,10,10,18,20] . Here the result will be index 4.


def lastOccurrenceBinarySearch(arr, k):  # T.C : O(logn) , S.C: O(1)
    low = 0
    high = len(arr) - 1
    res = 0
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            res = mid
            low = mid + 1  # To check the right half of the mid as we have to find the last occurrence.
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return res


# print(lastOccurrenceBinarySearch([2,4,10,10,10,18,20], 10))
# ----------------------------------------------------------------------------------------------------------------------
# QUESTION 14: Given a sorted array of n elements, possibly with duplicates. Find the number of occurrences of a number.

# The brute force approach will be using loops and incrementing the count as and when we find the element while traversing
# Time complexity: O(n), Space Complexity : O(1)
def countBruteForce(arr, k):
    count = 0
    for i in range(len(arr)):
        if arr[i] == k:
            count += 1
    return count


# The more efficient solution would be using binary search. Here we'll search the first and last occurrence seperately
# and then return the result

def countBinarySearch(arr, k):  # T.C: O(logn) S.C: O(1)
    low = firstOccurrenceBinarySearch(arr, k)
    high = lastOccurrenceBinarySearch(arr, k)
    return high - low + 1


# print(countBinarySearch([2,4,10,10,10,18,20], 10))
# ----------------------------------------------------------------------------------------------------------------------
# QUESTION 15: How many times is a sorted array rotated.
# Tip: If the array is clockwise rotated then the [len(arr)-indexOfMinElement] is the no times the array is rotated.
# Tip: If the array is anticlockwise rotated then the [indexOfMinElement[ is the no times the array is rotated.

# After the tip to find the min element we can use linear search. But the time complexity will be linear. Which is not
# efficient better we will use Binary Search.


def rotatedArrayBinarySearch(arr):
    result = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        next = (mid + 1) % len(arr)
        prev = (mid + len(arr) - 1) % len(arr)
        if arr[prev] >= arr[mid] and arr[next] > arr[mid]:
            result = mid
        if arr[high] >= arr[mid]:
            high = mid - 1
        elif arr[low] <= arr[mid]:
            low = mid + 1
    return len(arr) - result


# print(rotatedArrayBinarySearch([11,12,15,18,2,5,6,8]))
# -----------------------------------------------------------------------------------------------------------------------
# QUESTION 16: Find an element in a sorted rotated array.
# The brute force approach will use one loop to traverse the array and find the element. (Linear Time Complexity)

def findInSortedArray(arr, k):  # T.C : O(logn), S.C: O(1)
    n = len(arr)
    low = 0
    high = n - 1
    result = -1
    minElementIndex = -1
    while low <= high:
        mid = low + (high - low) // 2
        next = (mid + 1) % n
        prev = (mid + n - 1) % n
        if arr[prev] >= arr[mid] and arr[next] > arr[mid]:
            minElementIndex = mid
        if arr[mid] <= arr[high]:
            high = mid - 1
        elif arr[low] <= arr[mid]:
            low = mid + 1
    # Now as both the left and right array from the minElementIndex are sorted so we will use binary search on both sides.
    low = 0  # Checking on the left side of the minElementIndex
    high = minElementIndex - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            result = mid
            break
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    if result == -1:  # Checking on the right side of the minElementIndex
        low = minElementIndex
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == k:
                result = mid
                break
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
    return result


# print(findInSortedArray([11,12,15,18,2,5,6,8], 6))
# -----------------------------------------------------------------------------------------------------------------------
# QUESTION 17: Searching in a nearly sorted array.


def searchInNearlySortedArray(arr, k):                  # T.C : O(logn), S.C: O(1)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            return mid
        elif mid - 1 >= 0 and arr[mid - 1] == k:
            return mid - 1
        elif mid + 1 <= len(arr) - 1 and arr[mid + 1] == k:
            return mid + 1
        if arr[mid] < k:
            low = mid + 2
        elif arr[mid] > k:
            high = mid - 2


# print(searchInNearlySortedArray([5,10,30,20,40],20))
# ---------------------------------------------------------------------------------------------------------------------
# Question 18: Finding the floor of an element in a sorted array.
# Floor of an element is the greatest element smaller than the given element.


def searchFloor(arr, k):                                    # T.C : O(logn), S.C: O(1)
    result = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            result = k
        elif arr[mid] < k:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result, arr[result]


# print(searchFloor([1,2,3,4,8,10,10,12,19],5))
# ---------------------------------------------------------------------------------------------------------------------
# Question 19: Finding the ceiling of an element in a sorted array.
# Ceiling of an element is the smallest element greater than the given element.


def searchCeil(arr, k):                                       # T.C : O(logn), S.C: O(1)
    result = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            result = k
        elif arr[mid] > k:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result, arr[result]

# print(searchCeil([1,2,3,4,8,10,10,12,19],9))
