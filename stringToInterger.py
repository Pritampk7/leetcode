string = "-4193 with words"


def atoi(string):
    i = 0
    n = len(string)
    result = 0
    sign = 1


    while i < n and string[i] == ' ':
        i += 1

    if i < n and string[i] in ["+", "-"]:
        if string[i] == "-":
            sign = -1
        else:
            sign = 1
        i += 1
    while i < n and string[i].isdigit():
        digit = int(string[i])
        result = result * 10 + digit
        i += 1

    return sign * result


print(atoi(string))
