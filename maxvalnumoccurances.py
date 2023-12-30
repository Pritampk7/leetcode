# nums = [2, 7]


def countMaxvalocc(nums: list[int]) -> list:
    maxVal = nums[0]
    counter = 0
    for i, num in enumerate(nums):
        if num > maxVal:
            maxVal = num
            counter = 1
        elif num == maxVal:
            counter += 1

    return [maxVal, counter]


print(countMaxvalocc(nums=[2, 7, 7, 3, 9, 9, 9, 9]))
