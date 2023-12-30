nums = [2, 7, 11, 15]
target = 9


class twoSum:
    def findmaxtwosum(self, nums: list[int], target: int) -> list:

        hashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i


twosumobj = twoSum()
print(twosumobj.findmaxtwosum(nums, target))
