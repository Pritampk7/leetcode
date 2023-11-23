
"""
string1 = "dubble"
string2 = "bb"
"""


def substringIndex(string1: str, string2:str) -> int:

    for i in range(len(string1) - len(string2) +1):
        if string1[i:i + len(string2)] == string2:
            return True
    return False


string1 = "duboblebbb"
string2 = "bob"

print(substringIndex(string1, string2))