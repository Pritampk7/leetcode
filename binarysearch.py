class Solution:
    def binarySearch(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        print(l+ r//2)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid


nums = [-1, 0, 3, 5, 9, 12]
target = 9

obj = Solution()
print(obj.binarySearch(nums, target))
