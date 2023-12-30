def first_uniq_char(s):
    hashSet = {}
    for i in s:
        hashSet[i] = 1 + hashSet.get(i, 0)

    for index in range(len(s)):
        if hashSet[s[index]] == 1:
            return index
    return -1


# Test cases
print(first_uniq_char("leetcode"))  # Should return 0
print(first_uniq_char("novelette"))  # Should return 2
print(first_uniq_char("aabb"))          # Should return -1
