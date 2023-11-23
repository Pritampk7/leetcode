nums = [2, 7, 11, 8, 11, 8, 3, 11, 8, 9, 10]


def secondLargest(nums: list[int]) -> int:
    nums.sort()

    for item in range(len(nums) - 1, -1, -1):
        if nums[item - 1] != nums[item]:
            return nums[item - 1]


print(secondLargest(nums))
