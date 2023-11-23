'''
input = [1,1,0,1,1,1]
op: 3
'''

input = [1, 1, 0, 1, 1, 1]

count = 0
solution = 0
for i in input:
    if i == 1:
        count += 1
    else:
        solution = max(count, solution)
        count = 0

solution = max(count, solution)
print(solution)
