# 0 1 1 2 3 5 8 13

# Using recursion         T.C = O(2^n), S.C = O(n)  This is excessive recursion


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-2)+fib(n-1)


# Approach 2 = MEMOIZATION
# To avoid excessive recursion we use global variables and we use array to put the values at a particular position( here
# it is like once we find fib(2) then we don't find the find fib(2) in some other parts.
# T.C = O(n) and S.C = O(n)


lis = [-1] * 10


def fib1(n):
    global lis
    if n <= 1:
        return n
    else:
        if lis[n-2] == -1:
            lis[n-2] = fib1(n-2)
        if lis[n-1] == -1:
            lis[n-1] = fib(n-1)
        return lis[n-2] + lis[n-1]


print(fib1(7))

# Using iteration         T.C = O(n), S.C = O(1)


def fib2(n):
    t0 = 0
    t1 = 1
    result = 0
    if n <= 1:
        return n
    for i in range(2, n+1):
        result = t0 + t1
        t0 = t1
        t1 = result
    return result

