from math import *

def sieve(limit):
    numbers = range(2,limit+1)
    index_pointer = 0
    counter = 1
    lmt = ceil(sqrt(limit))
    while(index_pointer+1 <= len(numbers)):
        if(numbers[index_pointer] > lmt):
            return numbers
        for no in numbers[index_pointer+1:]:#numbers above the index pointer in        the list
            if(no%numbers[index_pointer]==0):
                numbers.pop(counter)
            else:
                counter +=1
        index_pointer += 1
        counter = index_pointer+1
    return numbers

def sum_2m():
    return sum(sieve(2000000))

def beta_sieve(limit):
    sqrtLimit = int(ceil(sqrt(limit)))
    sieve = [False]*(limit+1) #All numbers are not prime
    sieve[2] = True # Only 2 is a prime
    for x in xrange(3,limit,2):
        sieve[x] = True #set all odds to be true so u can eliminate below
    for x in xrange(3,sqrtLimit,2):
        if sieve[x]:#number is prime, eliminate all multiples!!
            startFrom = x*x
            for y in xrange(startFrom,limit,(2*x)):
                sieve[y] = False
    sumed = 0
    for n in xrange(2,limit):
        if sieve[n]:
            sumed = sumed + n 
    return sumed
a = beta_sieve(2000000)
