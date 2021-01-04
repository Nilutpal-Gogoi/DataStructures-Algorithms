# The power(or exponent) "a", of a number x represents the number of times x will
# be multiplied by itself. It is written as a small, superscript number to the
# right of and above the base number.


def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base*power(base, exponent-1)


# print(power(2,3))

# Better time complexity


def power1(base ,exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        return power1(base*base, exponent//2)
    else:
        return base*power1(base*base, (exponent-1)//2)


print(power1(2, 3))
