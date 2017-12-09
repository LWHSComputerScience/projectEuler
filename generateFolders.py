import os

for x in range(0,100):
    os.makedirs("Problem %s"%x)
    file = open("Problem %s/README.md"%x, "w+")
    file.write("Problem %s replace with problem description (https://projecteuler.net/problem=%s)"%(x,x))

