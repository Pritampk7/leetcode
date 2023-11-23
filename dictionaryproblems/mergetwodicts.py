dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}


# Expected Output: {'a': 1, 'b': 3, 'c': 4}

# my solution
def merge2dicts(dict1, dict2):
    new = {}
    for key, val in dict1.items():
        if key in dict2:
            new[key] = dict2.get(key)
        else:
            new[key] = val

    for key, val in dict2.items():
        if key not in dict1:
            new[key] = dict2.get(key)
    return new


# print(merge2dicts(dict1, dict2))

# correct solution
def mergedicts(dict1, dict2):
    merge = {**dict1, **dict2}
    return merge


print(merge2dicts(dict1, dict2))
