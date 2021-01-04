# e^x = 1 + (x/1) + (x^2/2!) + ... + n terms

# Since in finding summation, factorials and power the result we get is in returning part of the recursion but we can't
# do that in taylor series as it has both summation, factorial and power. So we use static or global variables as their
# value doesn't change in the recursion.


p, f = 1, 1


def taylor1(x, n):
    global p, f
    result = 0
    if n == 0:
        return 1
    else:
        result = taylor1(x, n-1)
        p = p * x
        f = f * n
        return result+(p/f)


# print(taylor1(1, 2))


# Approach 2 : HORNER's RULE
# Better time complexity

def horner_iter(x, n):
    result = 1
    while n > 0:
        result = 1 + (x/n)*result
        n -= 1
    return result


result = 1


def horner_rec(x, n):
    global result
    if n == 0:
        return result
    result = 1 + (x/n)*result
    return horner_rec(x, n-1)


print(horner_rec(1, 2))