class Solution:
    def distinctValues(self, nums: list[int]) -> int:
        nums.sort()
        distinct = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                distinct += 1
        return distinct


obj = Solution()
s = obj.distinctValues([8, 0, 6, 1, 9, 5])
print(s)
