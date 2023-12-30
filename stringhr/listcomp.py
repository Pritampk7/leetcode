if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    first = 0
    last = 0
    arr.sort()

    for num in arr:
        if num > last:
            if num > first:
                first, last = num, first
            else:
                last = num

    print(last)
