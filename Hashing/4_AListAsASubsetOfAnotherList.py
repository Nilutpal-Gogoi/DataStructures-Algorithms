# Implement the is_subset(list1, list2) function which will take two lists as input and check whether one list is the
# subset of the other using hash tables(without using issubset()).


def is_subset(list1, list2):
    list1 = list(set(list1))
    list2 = list(set(list2))
    for i in list2:
        if i in list1:
            continue
        else:
            return False
    return True


print(is_subset([9,4,7,1,-2,6,5], [7,1,-2]))

# Time complexity: O(m+n) where list1 has m elements and list2 has n elements.

