nums = [2,2,1]

def singleNum(nums: list[int]) -> list:
    singleNums = []
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i-1] != nums[i] and nums[i] not in singleNums:
            singleNums.append(nums[i])
    return singleNums

print(singleNum())