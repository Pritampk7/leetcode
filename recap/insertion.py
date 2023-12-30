from typing import List


class sort:
    def insertionSort(self, arr: list[int]) -> str | list[int]:

        for i in range(1, len(arr)):
            currentIndex = i
            while currentIndex > 0 and arr[currentIndex] < arr[currentIndex - 1]:
                arr[currentIndex], arr[currentIndex - 1] = arr[currentIndex - 1], arr[currentIndex]
                currentIndex -= 1
        return arr


sortObj = sort()

arr = [1, 9, 4, 3, 7]
print(sortObj.insertionSort(arr))
