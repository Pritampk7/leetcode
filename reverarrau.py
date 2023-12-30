arr = ['h', 'e', 'l', 'l', 'o']

l = 0
r = len(arr) - 1
while l <= r:
    arr[r], arr[l] = arr[l], arr[r]
    l += 1
    r -= 1
print(arr)
