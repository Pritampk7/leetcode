inputs = "A man, a plan, a canal: Panama"


def validPalindrome(inputs):
    s1 = ""
    for i in inputs:
        if i.isalnum():
            s1 += i.lower()

    return s1 == s1[::-1]


print(validPalindrome(inputs))
