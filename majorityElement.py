def MajorityElement(nums: list[int]):
    # nums = [3,2,3,3]
    # output = 3
    global num
    counter = 1
    nums.sort()
    solution = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            counter += 1
        else:
            counter = 1
        if counter > solution:
            solution, num = counter, nums[i - 1]

    return solution, num


print(MajorityElement([3, 2, 3]))
