import os

for x in range(0,100):
    os.makedirs("Problem %s"%str(x).zfill(3))
    file = open("Problem %s/README.md"%str(x).zfill(3), "w+")
    file.write("Problem %s replace with problem description (https://projecteuler.net/problem=%s)"%(x,x))

