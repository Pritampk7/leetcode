my_dict = {'apple': 5, 'orange': 2, 'banana': 7, 'grape': 1}

getKeyValue = [(key, value) for key, value in my_dict.items()]

for k in range(len(getKeyValue)):

    for j in range(len(getKeyValue)-1-k):
        if getKeyValue[j][1] > getKeyValue[j+1][1]:
            getKeyValue[j+1], getKeyValue[j] = getKeyValue[j], getKeyValue[j+1]
new = {key:value for key, value in getKeyValue}
print(new)