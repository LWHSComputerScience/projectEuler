__author__ = 'samschickler'
list_of_primes = [x for x in range(2, 2000001)]
num = len(list_of_primes)**(1/2.0)
counter = 0
while list_of_primes[counter]< num:
    list_of_primes = list_of_primes[:counter+1] + [x for x in list_of_primes[counter+1:] if x % list_of_primes[counter] != 0]
    # print(list_of_primes)
    print(counter)
    counter += 1
print(list_of_primes)
print(sum(list_of_primes))