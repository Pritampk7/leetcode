def lenoflastword(string: str) -> str:
    i = len(string) - 1
    lastWordLen = 0
    while string[i].isspace():
        i -= 1

    for i in range(i, 0, -1):
        if string[i] == " ":
            break
        lastWordLen += 1

    return lastWordLen


print(lenoflastword("this is test  "))
