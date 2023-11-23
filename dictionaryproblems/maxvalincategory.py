input_dict = {
    'Math': {'Alice': 88, 'Bob': 72, 'Charlie': 90},
    'Science': {'Alice': 92, 'Bob': 84, 'Charlie': 85},
    'English': {'Alice': 78, 'Bob': 88, 'Charlie': 95}
}
# Expected Output: {'Math': 'Charlie', 'Science': 'Alice', 'English': 'Charlie'}

new = {}
for key, value in input_dict.items():
    max_key = next(iter(value))
    for k in value:
        if value[k] > value[max_key]:
            max_key = k
        new[key] = max_key
print(new)
