# Printing Natural Numbers from 1 to n using DIRECT RECURSION


def printNaturalNumbers1(lowerRange, upperRange):
    # Base Case
    if lowerRange > upperRange:
        return
    print(lowerRange, end=" ")

    # Recursive Case
    printNaturalNumbers1(lowerRange+1, upperRange)


# printNaturalNumbers1(1,5)


# Printing Natural Numbers from 1 to n using INDIRECT RECURSION

def printNaturalNumbers(lowerRange, upperRange):
    if lowerRange <= upperRange :
        print(lowerRange,end=" ")
        lowerRange += 1
        helperFunction(lowerRange, upperRange)
    else:
        return


def helperFunction(lowerRange, upperRange):
    if lowerRange <= upperRange :
        print(lowerRange,end=" ")
        lowerRange += 1
        printNaturalNumbers(lowerRange, upperRange)
    else:
        return


printNaturalNumbers(1,5)

