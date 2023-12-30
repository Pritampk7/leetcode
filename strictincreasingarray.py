nums = [1, 3, 2, 4]
nums = [1, 2, 10, 5, 7]


def increasingArray(nums):
    for i in range(1, len(nums) - 1):
        if nums[i - 1] > nums[i]:
            curr = nums[i - 1]

    return True


print(increasingArray(nums))
