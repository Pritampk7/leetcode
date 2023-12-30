nums = [2, 7, 11, 8, 11, 8, 3, 11, 8, 9, 10, 12]


def secondLargest(nums: list[int]) -> int:
    nums.sort()

    for item in range(len(nums) - 1, -1, -1):
        if nums[item - 1] < nums[item]:
            return nums[item - 1]


# print(secondLargest(nums))


first_largest = second_largest = nums[0]

for num in nums:
    if num > first_largest:
        second_largest, first_largest = first_largest, num
    elif first_largest > num > second_largest:
        second_largest = num

print(second_largest)
