input_dict = {'a': 10, 'b': 5, 'c': 15}
threshold = 10


# Expected Output: {'a': 10, 'c': 15}
def valueThreshold(input_dict, threshold=10):
    newDict = {}
    for key, value in input_dict.items():
        if value >= threshold:
            newDict.update({key: value})
    return newDict


print(valueThreshold(input_dict))
