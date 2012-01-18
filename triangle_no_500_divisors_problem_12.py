from prime_number_module import *

sum = 1
counter = 1

while (num_factors(sum) < 501):
    counter = counter +1
    sum = sum + counter

print sum
