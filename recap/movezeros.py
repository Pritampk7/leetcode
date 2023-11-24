def movezero(arr):
    l = 0
    for r in range(len(arr)):
        if arr[r] != 0:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
    return arr


def movezero2(arr):
    l = 0
    for r in range(len(arr)):
        if arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
    return arr


print(movezero2([1, 0, 2, 0, 3]))
