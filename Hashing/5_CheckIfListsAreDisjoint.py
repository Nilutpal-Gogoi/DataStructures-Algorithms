# Implement a function to check whether two given lists are disjoint or not. Two lists are disjoint if there are no
# common elements between them. The assumption is that there are no duplicate elements in each list.


def is_disjoint(list1, list2):
    list1 = list(set(list1))
    list2 = list(set(list2))
    for i in list1:
        if i in list2:
            return False
    return True

# Time Complexity : O(m+n)
