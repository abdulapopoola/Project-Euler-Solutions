from math import *

def formula():
    pass

def brute_loop():
    a = 1
    b = 1 
    found = False
    while(True):        
        a = 1
        while (a <= 50):
            c_squared = (a*a) + (b*b)
            c = sqrt(c_squared)
            sums = a+b+c
            if (sqrt(c_squared).is_integer() and (1000%(sums)==0)):
                mul = 1000/sums
                return (a*b*c*mul*mul*mul)
            else:
                a = a + 1
        b = b + 1
