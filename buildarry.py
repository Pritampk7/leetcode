def buildArray(nums):
    # Create an array of the same length as nums
    ans = [0] * len(nums)

    # Iterate through the nums array
    for i in range(len(nums)):
        # For each index i, set ans[i] to nums[nums[i]]
        ans[i] = nums[nums[i]]

    return ans


print(buildArray(nums=[0, 2, 1, 5, 3, 4]))
