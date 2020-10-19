# Implement a function that takes an array "arr", a "testVariable" (containing the
# number to search) and "currentIndex" (containing the starting index) as parameters.
# This function should output the index of the first occurrence of testVariable in arr.
# If testVariable is not found in arr it should return -1.

# ITERATIVE METHOD


def firstOccurrence(arr, test_var, start_index):
    for i in range(start_index, len(arr)):
        if arr[i] == test_var:
            return i
    return -1


print(firstOccurrence([9, 8, 1, 8, 1, 7],1,3))


# RECURSIVE METHOD
def firstOccurrence_rec(arr, test_var, start_index):
    if arr[start_index] == test_var:
        return start_index
    elif arr[start_index] != test_var and start_index == len(arr)-1:
        return -1
    else:
        return firstOccurrence_rec(arr,test_var, start_index+1)


print(firstOccurrence_rec([9, 8, 1, 8, 1, 7],1,3))