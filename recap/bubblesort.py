from typing import List


class sort:
    def bubbleSort(self, arr: list[int]) -> str | list[int]:
        n = len(arr)
        flag = False
        for outer in range(n-1):
            for inner in range(0, n -1-outer):
                if arr[inner] > arr[inner + 1]:
                    arr[inner], arr[inner + 1] = arr[inner + 1], arr[inner]
                    flag = True

        if not flag:
            return "Already sorted"
        return arr


sortObj = sort()

arr = [1,5,4, 4,3]
print(sortObj.bubbleSort(arr))
