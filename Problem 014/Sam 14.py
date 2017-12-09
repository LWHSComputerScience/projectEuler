
def getNext(num):
    if num %2==0:
        return num/2
    return 3*num +1

def genSequence(number):
    orig = number
    length = 0
    while number != 1:
        number = getNext(number)
        length += 1
    return (orig, length)
list_of_results = []
for x in range(1, 1000000):
    print(x)
    list_of_results.append(genSequence(x))
def key(x):
    return x[1]
print(sorted(list_of_results, key=key, reverse=True)[0])