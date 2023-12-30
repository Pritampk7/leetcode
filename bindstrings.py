s1 = "abcd"
s2 = "efg"


def bind(s1, s2):
    i, j = 0, 0
    output = ""
    while i < len(s1) or j < len(s2):
        if i < len(s1):
            output += s1[i]
            i += 1
        if j < len(s2):
            output += s2[j]
            j += 1

    return output


print(bind(s1, s2))
