string = "abcabcab"


def repeatedSubstringPattern(s: str) -> bool:
    for index in range(1, len(s) + 1):
        if len(s) % index == 0:
            count = len(s) // index
            if s[:index] * count == s:
                return True
    return False


# Example usage
print(repeatedSubstringPattern(string))  # True

print(9 % 3)
