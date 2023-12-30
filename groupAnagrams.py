s = ["eat", "tea", "tan", "ate", "nat", "bat"]

class Anagrams:

    def checkAnagram(self, item, s):
        matches = []
        for i in s:
            if ''.join(sorted(item)) == ''.join(sorted(i)):
                if i not in matches:
                    matches.append(i)
        return matches

    def groupAnagrams(self, s):
        groups = []
        for i in s:
            data = self.checkAnagram(i, s)
            if data not in groups and data is not None:
                groups.append(data)
        return groups


obj = Anagrams()
print(obj.groupAnagrams(s))
