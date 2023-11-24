class Solution:
    def remove(self, arr: list[int], target: int) -> int:
        l = 0

        for r in range(len(arr)):
            if arr[r] == target:
                arr[l] = arr[r]
                l += 1
        return l
obj = Solution()
print(obj.remove([0, 1, 2, 2, 3, 0, 4, 2], target=2))
