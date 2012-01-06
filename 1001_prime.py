primes = [2]
no = 3

while (len(primes) != 10001):
    prime_number = True
    for x in primes:
        if no % x == 0:
            prime_number = False
            break
    if(prime_number):
        primes.append(no)
    no = no + 1

print primes[10000]

