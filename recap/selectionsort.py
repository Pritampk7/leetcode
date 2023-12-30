from typing import List


class sort:
    def selectionSort(self, customList: list[int]) -> str | list[int]:

        for i in range(len(customList)):
            currentMinIndex = i
            for j in range(i + 1, len(customList)):
                if customList[currentMinIndex] > customList[j]:
                    currentMinIndex = j
            customList[i], customList[currentMinIndex] = customList[currentMinIndex], customList[i]
        return customList


sortObj = sort()

arr = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(sortObj.selectionSort(arr))
