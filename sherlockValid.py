class Sherlock:
    def validString(self, s):
        hashMap = {}
        for i in s:
            hashMap[i] = 1 + hashMap.get(i, 0)
        maxval = float("-inf")
        maxKey = None

        for key, value in hashMap.items():
            if value > 1 and value > maxval:
                maxval = value
                maxKey = key

        new = {}
        news = ""

        for key, value in hashMap.items():
            if key == maxKey:
                value -= 1
            news += key * value
            new[key] = value
        values = list(new.values())
        for freq in range(1, len(values)):
            if values[freq - 1] - values[freq] != 0:
                return "No"
        return "YES"


s = "abc"

obj = Sherlock()
print(obj.validString(s))
