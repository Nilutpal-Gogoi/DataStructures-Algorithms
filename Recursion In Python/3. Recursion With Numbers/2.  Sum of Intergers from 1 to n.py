#  Find the sum of numbers from 1 to n using recursion.


def sumTill(targetNumber):
    if targetNumber == 1:
        return 1
    else:
        return sumTill(targetNumber-1)+targetNumber

print(sumTill(5))