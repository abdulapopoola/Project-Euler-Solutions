from math import *

numbers_list = []

for i in xrange(2,101):
    for j in xrange(2,101):
        no = pow(i,j)
        if no not in numbers_list:
            numbers_list.append(no)

print len(numbers_list)

'''
Alternative one-liner
'''

print len(set(a**b for a in xrange(2,101) for b in xrange(2,101)))
