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
    # merge = {**dict1, **dict2}
    merge = dict()
    for key, value in dict1.items():
        if key in merge:
            merge[key] = dict1.get(value)
            merge[key] = dict2.get(value)
        else:
            merge[key] = value

    #merge = {key: value for key, value in zip(dict1.items(), dict2.items()) }
    return merge


print(mergedicts(dict1, dict2))
t = (10,11,12)
#print(t[:1])
print(*t)