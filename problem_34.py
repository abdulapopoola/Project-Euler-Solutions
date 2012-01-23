'''
http://en.wikipedia.org/wiki/Factorion states that 
There are just four factorions (in base 10) and they are 1, 2, 145 and 40585
Simple enough! sum is 145 + 40585

Similar to problem 30

If n is a natural number of d digits that is a factorion, then 10*pow(d-1) <= n
< =9!d and this fails to hold for d >= 8. Thus n has 7 digits and the maximum sum of factorials of digits for a 7 digit number is 9!7 = 2,540,160, which is the upper bound.
'''


first_nine_factorials=[1,1,2,6,24,120,720,5040,40320,362880]

def sum_factorials(n):
    sums = 0
    while n > 0:
        remainder = n%10
        n = n / 10
        sums += first_nine_factorials[remainder]
    return sums

print sum(n for n in xrange(3,2540161) if sum_factorials(n) == n)

