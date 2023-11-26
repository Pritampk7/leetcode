def majorityelement(nums: list[int]):
    count = 1
    nums.sort()
    maxcount = 0
    current_ele = nums[0]
    for right in range(1, len(nums)):
        if nums[right] == nums[right - 1]:
            count += 1
        else:
            count = 1
        maxcount = max(maxcount, count)
        current_ele = nums[maxcount - 1]

    return maxcount, current_ele


print(majorityelement([2, 2, 2, 1, 1, 1, 1]))
