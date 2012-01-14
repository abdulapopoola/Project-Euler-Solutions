prime_numbers_list = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
prime_dict = dict.fromkeys(prime_numbers_list,1)
last_prime_number = prime_numbers_list[-1]

def _numberIsPrime(n): #Checks if n is a prime number
    noIsPrime = (n >=2 and 1) or 0
    for prime in prime_numbers_list:
        if prime * prime >= n: break
        if not n % prime:
            noIsPrime = 0
            break
    if(noIsPrime): prime_dict[n] = 1
    return noIsPrime

def _refresh(x): #updates list of primes to include up to x
    global last_prime_number
    while (last_prime_number <=x):
        last_prime_number += 1
        if not last_prime_number % 2 : continue
        if _numberIsPrime(last_prime_number):
            prime_numbers_list.append(last_prime_number) #prime_dict is updated in _numberIsPrime method

def prime(x): # returns the xth prime number
    global last_prime_number
    while len(prime_numbers_list) <= x:
        last_prime_number += 1
        if _numberIsPrime(last_prime_number):
            prime_numbers_list.append(last_prime_number)
    return prime_numbers_list[x]

def isPrime(x): #Check if a number is prime
    _refresh(x)
    return prime_dict.get(x,0)

def factors(n): #Get the prime factors of n as a list
    _refresh(n)
    counter, factor, list_of_factors = 0, prime_numbers_list[0], []
    while factor <= n:
        if not n % factor:
            list_of_factors.append(factor)
            n = n / factor
        else:
            counter = counter + 1
            factor = prime_numbers_list[counter]
    return list_of_factors

def num_factors(n):  #Get the number of factors n has including 1 and n itself
    number_of_factors = 1
    counter = 0
    while n > 1:
        count_for_one_prime = 1
        while not n % prime(counter):
           count_for_one_prime +=1
           n = n / prime(counter)
        number_of_factors = number_of_factors * count_for_one_prime
        counter = counter + 1
    return number_of_factors
    
