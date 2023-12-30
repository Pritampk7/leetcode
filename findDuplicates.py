from typing import Tuple, List

nums = [2, 3, 1, 1, 4, 3, 2, 1, 9, 9, 0]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def findDuplicates(nums: list[int]) -> tuple[int, list[int]]:
    duplicates = []
    count = 0
    nums.sort()

    for index in range(1, len(nums)):
        if nums[index - 1] == nums[index] and nums[index] not in duplicates:
            duplicates.append(nums[index])
            count += 1

    return count, duplicates


print(findDuplicates(nums))
