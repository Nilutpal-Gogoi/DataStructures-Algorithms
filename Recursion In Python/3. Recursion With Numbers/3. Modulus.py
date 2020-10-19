# Implement Modulo operation
#   10mod4=6mod4=2mod4
#   10mod4 = (10-4)mod4 = (10-4-4)mod4
# We can generalize this as follows:
# dividend  mod  divisor
# ⇒(dividend−divisor) mod divisor
#
# ⇒(dividend−divisor−divisor) mod divisor
# We can continue subtracting the divisor from the dividend until the dividend becomes
# less than the divisor. In this case, the remainder will be the dividend.
# This mathematical generalization
# dividend mod divisor = (dividend−divisor) mod divisor
# is our recursive case. The condition when the dividend is less than the divisor is
# our base case.


def modulo(dividend, divisor):
    if divisor < 0:
        print("Divisor cant be")
        return 0
    if dividend < divisor:
        return dividend
    else:
        return modulo(dividend-divisor, divisor)

print(modulo(13,5))