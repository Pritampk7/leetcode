s = "ahbd"
t = "ahbh"


def issubsequence(s, t):
    l, r = 0, 0
    if not s:
        return True
    while l < len(s) and r < len(t):
        if s[l] == t[r]:
            l += 1
        r += 1
    return len(s) == l


def isSubsequence(s: str, t: str) -> bool:
    left, right = 0, 0
    while left < len(s) and right < len(t):
        if s[left] == t[right]:
            left += 1
        right += 1
    return len(s) == left


def isssub(s: str, t: str) -> bool:
    left = 0
    for r in range(len(t)-1):
        if s[left] == t[r] and left < len(s):
            left += 1
    return left == len(s)


print(isssub(s, t))
print(isSubsequence(s,t))
print(issubsequence(s, t))