def containsDuplicate(arr: list[int]) -> bool:
    hashset = set()
    for num in arr:
        if num in hashset:
            return True
        hashset.add(num)
    return False


print(containsDuplicate([1, 2, 3, 4, 4]))
