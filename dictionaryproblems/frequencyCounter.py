input_str = "hello world"


# Expected Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def frequencyCounter(input_str):
    dictupdate = {}
    for st in input_str:
        if st in dictupdate:
            dictupdate[st] += 1
        else:
            dictupdate[st] = 1
    return dictupdate


print(frequencyCounter(input_str))
