__author__ = 'samschickler'
def genValues(e, x):
    list = []

    for t in range(e, x, 1):
        for g in range(e, x, 1):
            temp = t**g
            if temp in list:
                continue
            else:
                list.append(temp)

    return len(list)
print(genValues(2,101))