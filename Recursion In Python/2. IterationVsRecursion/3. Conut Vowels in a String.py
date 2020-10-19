# Imagine that we have to find the number of vowels in a given string. We know that the
# English alphabet contains 5 vowels: a, e, i, o, u. Solve the problem using iterative and
# recursive methods.


def isVowel(str):
    str = str.lower()
    vowels = "aeiou"

    if str in vowels:
        return 1
    else:
        return 0


def countVowels(str):
    count = 0
    for i in range(len(str)):
        if isVowel(string[i]):
            count += 1
    return count


def countVowels_rec(str, n):
    if n == 1:
        return isVowel(string[0])
    return isVowel(string[n-1]) + countVowels_rec(str, n-1)


string = "Educative"
print(countVowels_rec(string, len(string)))

