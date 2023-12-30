import rest_framework.serializers

input = [-4, -1, 0, 3, 10]


def sqauresorted(input) -> list:
    l = 0
    r = len(input) - 1
    new = []

    while l <= r:
        if input[l] ** 2 > input[r] ** 2:
            new.append(input[l] ** 2)
            l += 1
        else:
            new.append(input[r] ** 2)
            r -= 1

    return new[::-1]


print(sqauresorted(input))
