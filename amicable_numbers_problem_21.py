#Note that proper divisors are always less than n
def proper_divisors(n):
    return list(i for i in xrange(1,(n/2)+1) if not n%i)

sums_dict = dict((n,sum(proper_divisors(n))) for n in xrange(1,10000))

print sum(n for n in xrange(1, 10000) if sums_dict.get(sums_dict[n], 0) == n
and sums_dict[n] != n)


