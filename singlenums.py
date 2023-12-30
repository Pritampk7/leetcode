nums = [9, 1, 2, 1, 2, 7]
nums = [1, 2, 1, 2, 3, 5, 6]


def check(nums, i):
    if i > 0 and nums[i - 1] == nums[i]:
        return False
    if i < len(nums) - 1 and nums[i] == nums[i + 1]:
        return False
    return True


def singlenumber(nums):
    nums.sort()
    print(nums)
    for i in range(len(nums)):
        if check(nums, i):
            return nums[i]


print(singlenumber(nums))
