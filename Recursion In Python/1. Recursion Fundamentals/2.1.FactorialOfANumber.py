# Let's take a look at a recursive function that calculates the factorial of a number.
# A factorial is the product of an integer and all the postitive integers less than it.


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(5))