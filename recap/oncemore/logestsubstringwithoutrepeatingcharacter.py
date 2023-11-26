class solution:
    def longestsubstring(self, arr):
        hashset = set()
        left = 0
        res = 0
        for right in range(len(arr)):
            if arr[right] in hashset:
                hashset.remove(arr[left])
                left += 1
            hashset.add(arr[right])
            res = max(res, right - left + 1)
        return res


string = solution()
print(string.longestsubstring(arr="abcc"))
