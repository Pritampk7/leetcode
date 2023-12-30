s1, s2, s3 = 'ab', 'xyz', '12345'

i, j, k = 0, 0, 0

output = ""
while i < len(s1) or j < len(s2) or k < len(s3):

    if i < len(s1):
        output += s1[i]
        i += 1

    if j < len(s2):
        output += s2[j]
        j += 1

    if k < len(s3):
        output += s3[k]
        k += 1

print(output)
