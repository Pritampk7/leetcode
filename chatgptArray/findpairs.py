numbers = [1, 2, 3, 4, 5, 5, 0]
target = 5


def find_pairs(numbers, target):
    output = []
    for i in range(len(numbers)):
        for j in range(0, len(numbers)):
            if numbers[i] + numbers[j] == target and (numbers[j], numbers[i]) not in output:
                output.append((numbers[i], numbers[j]))

    return output


def find_pairs2(numbers, target):
    output = []
    sets = numbers
    for num in numbers:
        if target - num in sets:
            output.append((num, target - num))
            sets.remove(num)
    return output


print(find_pairs2(numbers, target))
