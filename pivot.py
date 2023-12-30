nums = [2, 3, -1, 8, 4]


def midleIndex(nums):
    total = sum(nums)
    leftsum = 0
    for i in range(len(nums)):
        righsum = total - nums[i] - leftsum
        if leftsum == righsum:
            return i
        leftsum += nums[i]
    return leftsum


print(midleIndex(nums))
