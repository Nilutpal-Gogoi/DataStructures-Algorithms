# Implement a function that takes two numbers, "testVariable1" and "testVariable2" and
# returns their greatest common divisor.


def GCD(test1, test2):
    if test1 == test2:
        return test1
    a = max(test1, test2)
    b = min(test1, test2)
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


print(GCD(6, 9))


# The process of calculating GCD is as follows: If m>n, then GCD(m,n) is the
# same as GCD(m-n,n). This statement is based on the premise that if m/d and
# n/d both leave no remainder, then (m-n)/d also leaves no remainder.
#
# def gcd(testVariable1, testVariable2) :
#   # Base Case
#   if testVariable1 == testVariable2 :
#     return testVariable1
#
#   # Recursive Case
#   if testVariable1 > testVariable2 :
#     return gcd(testVariable1 - testVariable2, testVariable2)
#   else :
#     return gcd(testVariable1, testVariable2 - testVariable1)
