def countstringcout(str1, str2):
    newstring = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            newstring += str1[i]
    return newstring


def concecutiveStrings(strings: list[str]):
    count = countstringcout(strings[0], strings[1])
    for c in range(2, len(strings)):
        count = countstringcout(count, strings[c])
    return count


print(concecutiveStrings(["nanny", "nanam", "naak"]))
