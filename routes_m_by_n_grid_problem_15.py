def factorial(m):
    mul = 1
    while (m > 1):
        mul = mul * m
        m = m - 1
    return mul

def routes(m,n):
    return factorial(m+n)/factorial(m)/factorial(n)
