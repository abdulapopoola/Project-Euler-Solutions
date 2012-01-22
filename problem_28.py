'''
n is the ring number; where n=1 is the ring 
7 8 9
6   2
5 4 3
Rightmost top corner of ring has value (2n+1)*(2n+1)
Leftmost top corner of ring has value ((2n+1)*(2n+1)) - 2n
Leftmost bottom corner of ring has value ((2n+1)*(2n+1)) - 2n - 2n
Rightmost bottom corner of ring has value ((2n+1)*(2n+1)) - 2n - 2n - 2n

Hence sum of diagonals for ring n is
4((2n+1)*(2n+1)) - 12n
'''

def ringSum(n):
    if n == 0:
        return 1
    return (4*(2*n + 1) * (2*n +1)) - (12*n)

def diagonalSum():
    sums = 0
    count = 0
    while (2*count+1) <= 1001:
        sums += ringSum(count)
        count +=1
    return sums

print diagonalSum()

    
