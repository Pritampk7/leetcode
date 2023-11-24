class Solution:
    def majorityElement(self, arr: list[int]):
        num = 0
        count = 0
        currentMax = 1
        arr.sort()
        print(arr)
        for i in range(len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
            else:
                count = 1
            if count > currentMax:
                currentMax, num = max(currentMax, count), arr[i - 1]
        return num, currentMax

 
majorityElement = Solution()
print(majorityElement.majorityElement([2, 1, 2, 1]))
