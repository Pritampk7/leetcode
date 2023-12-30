def formString(s) -> str:
    new = ""
    for i in range(1, len(s)):
        if s[i].isdigit():
            new += s[i - 1] * int(s[i])

    return new


s = 'a3z2b4'

print(formString(s))
