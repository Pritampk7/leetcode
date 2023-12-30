s = "hello world"
t = {'l', 'o'}


class CountChars:
    def countchar(self, s, t):
        CountS = {}
        for i in s:
            CountS[i] = 1 + CountS.get(i, 0)

        num = 0
        for i in t:
            num += CountS.get(i, 0)
        return num


countObj = CountChars()
print(countObj.countchar(s, t))
