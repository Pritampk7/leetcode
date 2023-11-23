def twosum(arr, target):
    hashmap = {}
    for index in range(len(arr)):
        diff = target - arr[index]
        if diff in hashmap:
            return hashmap[diff], index
        hashmap[arr[index]] = index


arr = [2, 1, 4, 2, 7, 3]

target = 10
print(twosum(arr, target))
