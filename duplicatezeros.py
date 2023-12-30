arr = [1, 0, 2, 3, 0, 4, 5, 0]

# Output: [1,0,0,2,3,0,0,4]

l = 0
r = len(arr) - 1

while l < r:
    if arr[l] == 0:
        arr[l + 1] = 0
        l = l + 1
    l += 1

print(l, arr)
