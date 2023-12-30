s = ["a", 1, 'b', 2, "c", 3, "d", 4]

def formDict(s):
    newDict = {}
    for i in range(1, len(s), 2):
        newDict[s[i]] = s[i-1]
    return newDict

print(formDict(s))