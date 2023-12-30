nums = [4,3,2,1]

from functools import reduce


def calculate(ele, nums):
    multi = 1
    copylist = nums[:]
    copylist.remove(nums[ele])
    for i in copylist:
        multi *= i
    return multi


def product(nums):
    newArr = []
    for i in range(len(nums)):
        data = calculate(i, nums)
        newArr.append(data)

    return newArr


print(product(nums))
