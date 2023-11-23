input_dict = {'item1': 'banana', 'item2': 'apple', 'item3': 'grape', 'item4': 'melon', 'item5': 'pear'}
# Expected Output: {'item1': 'banana', 'item2': 'apple', 'item3': 'grape'}


new = {key: value for key, value in input_dict.items() if 'a' in value}

print(new)