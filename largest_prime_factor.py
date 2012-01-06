from math import *

no = 600851475143
sqrtt = sqrt(no)
list_of_primes = []

for i in xrange(2,int(ceil(sqrtt))):
    if ((no % i) == 0):
        prime_no = True
        for num in list_of_primes:
            if((i % num)==0):
                prime_no = False
                break
        if(prime_no):
            list_of_primes.append(i)

print max(list_of_primes)


    



