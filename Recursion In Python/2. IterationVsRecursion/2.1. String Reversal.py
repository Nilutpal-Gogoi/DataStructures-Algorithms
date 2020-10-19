# ---------------- Iterative Process ------------------------------------------

def reverseString(string):
    reverse = ''
    length = len(string) - 1
    while length>=0:
        reverse = reverse + string[length]
        length = length-1

    return reverse

# print(reverseString("Educative"))

# ---------------- Recursive Process -------------------------------------------


def reverseString_rec(string):
    # Base condition
    if len(string)==0:
        return string
    # Recursive Case
    else:
        return reverseString_rec(string[1:])+string[0]


print(reverseString_rec("Educative"))


