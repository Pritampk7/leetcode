def removeElement(nums: list[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], val=2))
