def maxsumsubarry(arr: list[int]) -> int:
    currentmaxSum = arr[0]
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            maxsum = sum(arr[i: j + 1])
            currentmaxSum = max(currentmaxSum, maxsum)
    return currentmaxSum


def maxsumsubarry2(arr: list[int]) -> int:
    currentMax = arr[0]
    currentSum = 0
    for num in arr:
        if currentSum < 0:
            currentSum = 0
        currentSum += num
        currentMax = max(currentSum, currentMax)
    return currentMax


print(maxsumsubarry2([-2, -5, 6, -2, -3, 1, 5, -6]))
