def longestsubsrting(s):
    charset = set()
    l = 0
    res = 0
    for r in range(len(s)):
        if s[r] in charset:
            charset.remove(s[l])
            l += 1
        charset.add(s[r])
        res = max(res, r - l + 1)

    return res, charset


s = 'abracadabra'
print(longestsubsrting(s))
