# Implement a function that takes a specific number "testVariable" and returns the
# square of the number.
# use the following mathematical identity to solve this problem:
# (n-1)^2 = n^2 - (2*n) + 1


def recursion_square(n):
    if n == 0:
        return 0
    else:
        return recursion_square(n - 1) + (2 * n) - 1


# To implement the square operation as a recursive function, we first need to express
# the square operation in terms of itself. So we convert the above equation as:
# n^2 = (n-1)^2 + 2*n - 1

print(recursion_square(5))

# The iterative method will be:
def square(n):
    return n*n
