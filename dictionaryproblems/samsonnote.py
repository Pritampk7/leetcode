from collections import defaultdict
def ransom():
    ransomNote = 'aa'
    magazine = 'aab'
    ransomdict = defaultdict(int)
    magazindict = defaultdict(int)
    for char in ransomNote:
        ransomdict[char] = 1 + ransomdict.get(char, 0)

    for char in magazine:
        magazindict[char] = 1 + magazindict.get(char, 0)

    for i in range(ord('a'), ord('z') + 1):
        char = chr(i)
        if ransomdict[char] > magazindict[char]:
            return False
    return True


print(ransom())



