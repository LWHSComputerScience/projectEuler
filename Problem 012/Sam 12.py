__author__ = 'samschickler'
def factors(x):
    factor = 0
    g = 1
    while g < x**(1/2.0):
        if x%g == 0:
            factor += 1
        g += 1
    if x% x**(1/2.0)==0:
        factor+=.5
    return factor*2
startNum = 10
while True:
    print(startNum*(startNum+1)/2)
    if factors(startNum*(startNum+1)/2) > 500:
        break
        print(startNum)
    startNum+=1

