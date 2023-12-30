
print(ord('e'))
def formstring(s):
    new = ""
    for char in s:
        if char.isalpha():
            new += char
            temp = char
        else:
            digit = int(char)
            new += chr(ord(temp) + digit)
    return new


s = "a4k3b2"
print(formstring(s))
