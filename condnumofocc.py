string = "aaabbbcccd"


def countnumofocc(string):
    count = 1

    newstr = ''

    r = len(string)
    for i in range(1, r):
        if string[i - 1] == string[i]:
            count += 1
        else:
            newstr += string[i - 1] + str(count)
            count = 1

    newstr += string[-1] + str(count)

    return newstr


print(countnumofocc(string))
