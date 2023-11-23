input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 1}


# Expected Output: {1: 'c', 2: 'b'}

def inverDict(input_dict):
    new = {}
    for key, value in input_dict.items():
        new[value] = key

    return new


print(inverDict(input_dict))
