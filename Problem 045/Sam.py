__author__ = 'samschickler'
# def check_tri(x):
#     return ((8*x+1)**(1/2.0)+1) % 2 == 0
# def check_pent(x):
#     return ((24*x+1)**(1/2.0)+1)%6 == 0
# def check_hex(x):
#     return ((8*x+1)**(1/2.0)+1) % 4 == 0
# print(check_hex((1*(1+1)/2)))
#
# print([(x*(x+1)/2) for x in range(0, 100000) if check_hex((x*(x+1)/2)) and check_pent((x*(x+1)/2))])
# print([x*(2*x-1) for x in range(0, 100000) if check_tri(x*(2*x-1)) and check_pent(x*(2*x-1))])
# print([x*(2*x-1) for x in range(0, 100000) if check_pent(x*(2*x-1))])
# (x*(x+1)/2) this is the formula for hex numbers
print([x*(2*x-1) for x in range(0, 100000) if ((24*(x*(2*x-1))+1)**(1/2.0)+1)%6 == 0][2])

