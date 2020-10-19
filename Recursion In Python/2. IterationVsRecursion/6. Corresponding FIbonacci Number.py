# Implement a function that takes a variable(testVariable) and finds the number that
# is placed at that index in the Fibonacci sequence




def Fibonacci_iter(testVariable):
    first = 0
    second = 1
    testVariable = testVariable - 1
    while testVariable:
        total = first + second
        first = second
        second = total
        testVariable -= 1
    return second

# print(Fibonacci_iter(7))


def Fibonacci_rec(test_Var):
    first = 0
    second = 1
    if test_Var == 0:
        return 0
    elif test_Var == 1:
        return 1
    else:
        return Fibonacci_rec(test_Var-2) + Fibonacci_rec(test_Var-1)
print(Fibonacci_rec(7))
