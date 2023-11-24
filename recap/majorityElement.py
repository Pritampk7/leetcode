class Solution:
    def majorityElement(self, arr: list[int]):
        elements = {}
        maxcount, res = 0, 0
        for ele in arr:
            if ele not in elements:
                elements[ele] = 1 + elements.get(ele, 0)
                res = ele if elements[ele] > maxcount else res
                maxcount = max(elements[ele], maxcount)

        return res


majorityElement = Solution()
print(majorityElement.majorityElement([2, 2, 1, 2, 2]))
