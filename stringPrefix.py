s = "iloveleetcode"
words = ["apples","i","love","leetcode"]

def stringprefix(s, words):
    word = ""
    for i in words:
        word = word + i
        if word == s:
            return True
    return False

print(stringprefix(s, words))