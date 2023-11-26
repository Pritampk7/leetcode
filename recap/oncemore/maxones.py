def maxones(nums: list[int]) -> int:
    count = 0
    maxocc = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            count = 0
        maxocc = max(maxocc, count)

    return maxocc


print(maxones([1, 1, 0, 1, 1, 1]))
