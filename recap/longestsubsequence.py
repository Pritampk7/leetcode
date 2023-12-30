values = [0, 1, 0, 3, 2, 3]


def lis(values):
    LIS = [1] * len(values)
    for i in range(len(values) - 1, -1, -1):
        for j in range(i + 1, len(values)):
            if values[i] < values[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS), LIS


print(lis(values))
