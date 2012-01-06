def isPalindrome(number):   
    numberList = (str(number))
    return numberList == numberList[::-1]

for no1 in xrange(1,1000):
    for no2 in xrange(1,1000):
        numbera = no1*no2
        if (str(no1*no2)==str(no1*no2)[::-1]):
            numbers.append(numbera)

print max(numbers)
