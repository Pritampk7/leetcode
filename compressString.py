s = "aabcccccaaa"


def comperesString(s):
    compressed = []

    prev_char = s[0]
    count = 0
    for i in range(len(s)):
        if s[i - 1] == s[i]:
            count += 1
        else:
            compressed.append(prev_char + str(count))
            prev_char = s[i-1]
            count = 1
    compressed.append(s[-1] + str(count))
    compressed_str = ''.join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

print(comperesString(s))
print(comperesString("abcdef"))
