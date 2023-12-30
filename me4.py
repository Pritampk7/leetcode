arr = [1, 2, 2, 3, 3, 4, 3]

count = 0
res = 0
counter = 0
for num in arr:
    if count == 0:
        res = num
    if res == num:
        count += 1
        counter += 1
    else:
        count -= 1

print(res, counter)
