'''
4*(9**5) = 236196 
5*(9**5) = 295245
6*(9**5) = 354394
7*(9**5) = 413343 #So the highest possible sum of a 7-digit no is 6 digits
(which is less than the original 7 digit no) so the upper limit is 6
'''

def sum_powers(n,power):
    sums = 0
    while n > 0:
        remainder = n % 10
        n = n / 10
        sums = sums + (remainder ** power)
    return sums

print sum(n for n in xrange(2,354394) if sum_powers(n,5) == n)
    
