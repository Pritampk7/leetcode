import pdb


def maxarray(nums: list[int]) -> int:
    current_sum = nums[0]
    maxsum = 0
    for i in nums:
        if maxsum < 0:
            maxsum = 0
        maxsum += i
        current_sum = max(current_sum, maxsum)
    return current_sum


print(maxarray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
