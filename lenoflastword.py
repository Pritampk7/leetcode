def lenoflastword(string: str) -> str:
    i = len(string) - 1
    lastWordLen = 0
    while string[i] == " ":
        i -= 1
    for char in range(i, 0, -1):
        if string[char] == " ":
            break
        lastWordLen += 1
    return lastWordLen


print(lenoflastword("this is test  "))
