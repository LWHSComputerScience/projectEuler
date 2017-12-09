__author__ = 'samschickler'
for a in range(0, 700):
    for b in range(0, 700):
        # print((a**2+b**2)**(1/2.0))
        if (a**2+b**2)**(1/2.0) % 1 == 0 and (a**2+b**2)**(1/2.0)+ a +b==1000:
            print(a*b*((a**2+b**2)**(1/2.0)))