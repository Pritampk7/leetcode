def merge():
    arr1 = [1, 2, 3, 6, 6, 8]
    m = 3
    n = 3
    arr2 = [2, 5, 6]

    last = m + n - 1
    # expected arr1 = [1,1,2,2,3,4,4,5]

    while m > 0 and n > 0:
        if arr1[m - 1] > arr2[n - 1]:
            arr1[last] = arr1[m - 1]
            m -= 1
        else:
            arr1[last] = arr2[n - 1]
            n -= 1
        last -= 1
    while n > 0:
        arr1[last] = arr2[n - 1]
        n, last = n - 1, last - 1

    return arr1


print(merge())
