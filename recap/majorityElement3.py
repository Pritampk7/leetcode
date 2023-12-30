def majorityelement3(arr):
    res, count = 0, 0

    for num in arr:
        if count == 0:
            res = num
        if res == num:
            count += 1
        else:
            count -= 1

    return res


print(majorityelement3(arr=[3, 2, 2, 3, 3, 2, 2, 3, 3]))
