"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
	1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def fib(n): #Fibonacci formula that returns immediately; no recursion
    fterm = (((1 + sqrt(5))/2)**n)/sqrt(5)
    sterm = (((1 - sqrt(5))/2)**n)/sqrt(5)
    return fterm - sterm

"""The series given in this euler question start from the 3rd number of the fib sequence"""
def summer():
	sums = 0    
	count = 3
	while(fib(count) < 4000000): #Check that value is less than 4 million
		if(floor(fib(count) % 2) == 0.0): #Get even numbers
			sums = sums + fib(count)
		count = count + 1
	return sums
    	