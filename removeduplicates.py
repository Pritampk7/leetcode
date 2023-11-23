class Solution:
    def removeDuplicates(self, arr: list[int]) -> int:
        l = 1
        for r in range(1, len(arr)):
            if arr[r] != arr[r - 1]:
                arr[l] = arr[r]
                l += 1
        return l


duplicates = Solution()
print(duplicates.removeDuplicates(arr=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
