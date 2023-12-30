arr = [1, 3, 4, 0, 2, 0]


# ouput = [1,2,3,4,0,0]
def movezero(arr):
    last = 0
    for right in range(len(arr)):
        if arr[right]:
            arr[last], arr[right] = arr[right], arr[last]
            last += 1

    return arr

def movezero2(arr):
    last = 0
    for right in range(len(arr)):
        if arr[right]:
            arr[right], arr[last] = arr[last], arr[right]
            last += 1
    return arr


print(movezero2(arr))
