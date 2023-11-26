def single(nums, right):
    if right > 0 and nums[right] == nums[right - 1]:
        return False
    if right < len(nums) and nums[right] == nums[right + 1]:
        return False
    return True


def singlenum(nums):
    nums.sort()
    for right in range(len(nums)):
        if single(nums, right):
            return nums[right]


print(singlenum([1, 3, 4, 6, 1]))
