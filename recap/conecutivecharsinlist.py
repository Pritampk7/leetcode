input_arr = ["flower", "flow", "flow"]


def LCM(str1, str2):
    length = min(len(str1), len(str2))
    occ = ""
    for i in range(length):
        if str1[i] != str2[i]:
            break
        occ += str1[i]
    return occ


def concecutive(input_arr):
    sequence = LCM(input_arr[0], input_arr[1])

    for i in range(2, len(input_arr)):
        sequence = LCM(sequence, input_arr[i])
    return sequence


print(concecutive(input_arr))
