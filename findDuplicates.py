nums = [2, 3, 1, 1, 4, 3, 2, 1, 9, 9, 0]


def findDuplicates(nums: list[int]) -> list:
    duplicates = []
    nums.sort()
    print(nums)
    for index in range(1, len(nums)):
        if nums[index - 1] == nums[index] and nums[index] not in duplicates:
            duplicates.append(nums[index])

    return duplicates


print(findDuplicates(nums))
