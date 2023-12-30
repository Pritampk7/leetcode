def transform_string(s):
    letterCount = {}
    newString = ""
    for i in s:
        letterCount[i] = 1 + letterCount.get(i, 0)

    maxvalue = list(letterCount.values())[0]
    for key, val in letterCount.items():
        if val > maxvalue:
            maxvalue = val
            maxkey = key

    for i in s:
        if i == maxkey:
            newString += "a" if i.lower() == 'z' else chr(ord(i) + 1)
        else:
            newString += i
    return letterCount, newString


print(transform_string("hello world"))
