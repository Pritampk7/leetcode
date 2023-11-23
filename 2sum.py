def twsum(nums: list[int], target):
    records = {}

    for index, value in enumerate(nums):
        diff = target - value
        if diff in records:
            return records[diff], index
        records[value] = index


print(twsum([2, 1, 4, 2], 6))
