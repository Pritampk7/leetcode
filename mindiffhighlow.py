class MicDiff:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

    def findKDiff(self):
        self.nums.sort()
        r = self.k - 1
        l = 0
        res = float("inf")
        for i in range(r, len(nums)):
            res = min(res, nums[i] - nums[l])
            l += 1
        return res

    def secondsol(self):
        self.nums.sort()
        r = self.k - 1
        l = 0
        res = float("inf")

        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l, r = l+1, r + 1
        return  res


nums = [9, 4, 1, 7]
clsObj = MicDiff(nums, 1)
print(clsObj.findKDiff())
print(clsObj.secondsol())
