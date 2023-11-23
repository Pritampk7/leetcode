arr = [1, 0, 1, 1, 1, 1, 0, 1]


def maxconcecutiveones(arr):
    count = 0
    sol = 0
    for num in arr:
        if num == 1:
            count += 1
        else:
            sol = max(count, sol)
            count = 0

    return sol, count


print(maxconcecutiveones(arr))
